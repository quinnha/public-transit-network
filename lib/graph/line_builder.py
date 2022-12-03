
import csv
import os

# Builds a dictionary of lines from a CSV file


class LineBuilder():
    def __init__(self):
        # getting line information and storing as a key:value pair
        lines_list = []
        line_dic = {}
        station_path = os.path.dirname(__file__)
        station_path = os.path.join(
            station_path, "../../_dataset/london.lines.csv"
            )
        with open('_dataset/london.lines.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:

                lines_list.append(' '.join(row).replace("\"", "").split(','))

        # Remove header
        lines_list = lines_list[1:]

        for line in lines_list:
            line_id, name, colour, stripe = int(
                line[0]), line[1], line[2], line[3]
            line_dic[line_id] = [name, colour, stripe]
        self.lines = line_dic

    def display(self):
        print("\nLines:\n")
        for key in self.lines.keys():
            print(key, " - ", self.lines[key])
