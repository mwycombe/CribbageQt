/********************************************************************************
** Form generated from reading UI file 'CribbageV1.1.ui'
**
** Created by: Qt User Interface Compiler version 6.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef CRIBBAGEV1_H
#define CRIBBAGEV1_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Master
{
public:
    QWidget *TopContainer;
    QFrame *sessionFrame;
    QFrame *clubFrame;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout_3;
    QLabel *clubNumberLabel;
    QLabel *clubNameLabel;
    QLabel *clubPlayersLabel;
    QLabel *clubSeasonLabel;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout_4;
    QLabel *clubNumber;
    QLabel *clubName;
    QLabel *clubPlayers;
    QLabel *clubSeason;
    QFrame *playerActivityFrame;
    QWidget *layoutWidget2;
    QVBoxLayout *verticalLayout_5;
    QLabel *playersF1ActivityLabel;
    QLabel *playersF2ActivityLabel;
    QLabel *playersF3ActivityLabel;
    QLabel *playersF9ActivityLabel;
    QLabel *playersF10ActivityLabel;
    QLabel *playersEscActivityLabel;
    QLabel *playersDoubleClickActivityLabel;
    QLabel *clubFrameLabel;
    QLabel *activityFrameLabel;
    QLabel *SessionFrameLabel;
    QTabWidget *playersTab;
    QWidget *PlayersTab;
    QFrame *frame;
    QLabel *label;
    QLabel *activePlayerLabel;
    QCheckBox *showAllPlayers;
    QListWidget *playersList;
    QFrame *newPlayerFrame;
    QLabel *newEditPlayerLabel;
    QFrame *frame_3;
    QFormLayout *formLayout;
    QVBoxLayout *verticalLayout;
    QLabel *firstNameLabel;
    QLabel *lastNameLabel;
    QLabel *streetLabel;
    QLabel *cityLabel;
    QLabel *stateLabel;
    QLabel *zipLabel;
    QLabel *phoneLabel;
    QLabel *emailLabel;
    QLabel *accNumberLabel;
    QLabel *expiresLabel;
    QLabel *joinedLabel;
    QLabel *activeLabel;
    QWidget *layoutWidget3;
    QVBoxLayout *verticalLayout_2;
    QLineEdit *playerFirstNameEntry;
    QLineEdit *playerLastNameEntry;
    QLineEdit *playerStreetEntry;
    QLineEdit *playerCityEntry;
    QLineEdit *playerStateEntry;
    QLineEdit *playerZipEntry;
    QLineEdit *playerPhoneEntry;
    QLineEdit *playerEmailEntry;
    QLineEdit *playerACCNumberEntry;
    QLineEdit *playerExpiresEntry;
    QLineEdit *playerJoinedEntry;
    QLineEdit *playerActiveEntry;
    QWidget *tourneysTab;
    QFrame *frame_2;
    QLabel *label_3;
    QLabel *label_2;
    QFrame *frame_4;
    QListWidget *existingTouneysList;
    QWidget *layoutWidget4;
    QHBoxLayout *horizontalLayout;
    QLabel *label_6;
    QLabel *label_5;
    QLabel *label_7;
    QLabel *label_4;
    QFrame *frame_5;
    QFrame *frame_6;
    QLabel *label_9;
    QLabel *label_10;
    QFrame *frame_7;
    QLabel *newTourneyNumberLabel;
    QLabel *newTourneyDateLabel;
    QLineEdit *newTourneNumber;
    QLineEdit *newTourneyDate;
    QLabel *newTourneyLabel;
    QLabel *createTourneyLabel;
    QWidget *resultsTab;
    QFrame *frame_8;
    QFrame *frame_9;
    QLabel *resultsTouneyDateLabel;
    QLabel *resultsTounryNumberLabel;
    QLabel *resultsTourneyCountLabel;
    QLabel *resultsTourneyDate;
    QLabel *resultsTourneyNumber;
    QLabel *resultsTourneyCount;
    QFrame *frame_10;
    QLabel *label_27;
    QLabel *label_28;
    QLabel *label_29;
    QLabel *label_30;
    QLabel *label_31;
    QLabel *resultsSpreadPlus;
    QLabel *resultsSpreadMinus;
    QLabel *resultsSpreadDiff;
    QLabel *resultsSkunksPlus;
    QLabel *resultsSpreadMinus_2;
    QLabel *resultsSkunksDiff;
    QFrame *frame_11;
    QListWidget *resultsPlayList;
    QLabel *resultsPointsLabel;
    QLabel *resultsPlayerNameLabel_2;
    QFrame *frame_12;
    QLabel *resultsPlayerNameLabel;
    QLabel *label_42;
    QLabel *label_43;
    QLabel *label_44;
    QLabel *label_45;
    QLabel *label_46;
    QListWidget *tourneyResultsList;
    QFrame *frame_13;
    QLabel *resultPlayerNameLabel;
    QLabel *resultsPlayerName;
    QLineEdit *resultPlayerGp;
    QLineEdit *resutlPlayerGw;
    QLineEdit *resultPlayerSprd;
    QLineEdit *resultPlayerTkn;
    QLineEdit *resultPlayerDollars;
    QLineEdit *resultPlayerGiven;
    QWidget *layoutWidget5;
    QHBoxLayout *horizontalLayout_2;
    QLabel *resultGpLabel;
    QLabel *resultGwLabel;
    QLabel *resultSprdLabel;
    QLabel *resultTknLabel;
    QLabel *resultDollarLabel;
    QLabel *resultGvnLabel;
    QLabel *label_40;
    QLabel *label_14;
    QWidget *reportsTab;
    QFrame *frame_14;
    QListWidget *tourneysList;
    QFrame *frame_15;
    QCheckBox *checkBox;
    QPushButton *pushButton;
    QWidget *layoutWidget6;
    QVBoxLayout *verticalLayout_6;
    QCheckBox *checkBox_2;
    QCheckBox *checkBox_3;
    QCheckBox *checkBox_4;
    QCheckBox *checkBox_5;
    QCheckBox *checkBox_6;
    QCheckBox *checkBox_8;
    QCheckBox *checkBox_7;
    QCheckBox *checkBox_9;
    QCheckBox *checkBox_10;
    QLabel *label_23;
    QLabel *label_24;

    void setupUi(QMainWindow *Master)
    {
        if (Master->objectName().isEmpty())
            Master->setObjectName("Master");
        Master->resize(1114, 879);
        QFont font;
        font.setPointSize(12);
        font.setWeight(QFont::Medium);
        Master->setFont(font);
        TopContainer = new QWidget(Master);
        TopContainer->setObjectName("TopContainer");
        sessionFrame = new QFrame(TopContainer);
        sessionFrame->setObjectName("sessionFrame");
        sessionFrame->setGeometry(QRect(10, 20, 1091, 271));
        sessionFrame->setFrameShape(QFrame::Shape::Box);
        sessionFrame->setFrameShadow(QFrame::Shadow::Raised);
        sessionFrame->setLineWidth(3);
        clubFrame = new QFrame(sessionFrame);
        clubFrame->setObjectName("clubFrame");
        clubFrame->setGeometry(QRect(10, 20, 311, 241));
        clubFrame->setFrameShape(QFrame::Shape::Panel);
        clubFrame->setFrameShadow(QFrame::Shadow::Sunken);
        clubFrame->setLineWidth(2);
        layoutWidget = new QWidget(clubFrame);
        layoutWidget->setObjectName("layoutWidget");
        layoutWidget->setGeometry(QRect(20, 20, 123, 136));
        verticalLayout_3 = new QVBoxLayout(layoutWidget);
        verticalLayout_3->setObjectName("verticalLayout_3");
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        clubNumberLabel = new QLabel(layoutWidget);
        clubNumberLabel->setObjectName("clubNumberLabel");
        clubNumberLabel->setFrameShape(QFrame::Shape::Box);
        clubNumberLabel->setFrameShadow(QFrame::Shadow::Sunken);
        clubNumberLabel->setLineWidth(2);
        clubNumberLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout_3->addWidget(clubNumberLabel);

        clubNameLabel = new QLabel(layoutWidget);
        clubNameLabel->setObjectName("clubNameLabel");
        clubNameLabel->setFrameShape(QFrame::Shape::Box);
        clubNameLabel->setFrameShadow(QFrame::Shadow::Sunken);
        clubNameLabel->setLineWidth(2);
        clubNameLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout_3->addWidget(clubNameLabel);

        clubPlayersLabel = new QLabel(layoutWidget);
        clubPlayersLabel->setObjectName("clubPlayersLabel");
        clubPlayersLabel->setFrameShape(QFrame::Shape::Box);
        clubPlayersLabel->setFrameShadow(QFrame::Shadow::Sunken);
        clubPlayersLabel->setLineWidth(2);
        clubPlayersLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout_3->addWidget(clubPlayersLabel);

        clubSeasonLabel = new QLabel(layoutWidget);
        clubSeasonLabel->setObjectName("clubSeasonLabel");
        clubSeasonLabel->setFrameShape(QFrame::Shape::Box);
        clubSeasonLabel->setFrameShadow(QFrame::Shadow::Sunken);
        clubSeasonLabel->setLineWidth(2);
        clubSeasonLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout_3->addWidget(clubSeasonLabel);

        layoutWidget1 = new QWidget(clubFrame);
        layoutWidget1->setObjectName("layoutWidget1");
        layoutWidget1->setGeometry(QRect(150, 22, 141, 136));
        verticalLayout_4 = new QVBoxLayout(layoutWidget1);
        verticalLayout_4->setObjectName("verticalLayout_4");
        verticalLayout_4->setContentsMargins(0, 0, 0, 0);
        clubNumber = new QLabel(layoutWidget1);
        clubNumber->setObjectName("clubNumber");
        clubNumber->setStyleSheet(QString::fromUtf8("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";"));
        clubNumber->setFrameShape(QFrame::Shape::Box);
        clubNumber->setFrameShadow(QFrame::Shadow::Sunken);
        clubNumber->setLineWidth(2);

        verticalLayout_4->addWidget(clubNumber);

        clubName = new QLabel(layoutWidget1);
        clubName->setObjectName("clubName");
        clubName->setStyleSheet(QString::fromUtf8("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";"));
        clubName->setFrameShape(QFrame::Shape::Box);
        clubName->setFrameShadow(QFrame::Shadow::Sunken);
        clubName->setLineWidth(2);

        verticalLayout_4->addWidget(clubName);

        clubPlayers = new QLabel(layoutWidget1);
        clubPlayers->setObjectName("clubPlayers");
        clubPlayers->setStyleSheet(QString::fromUtf8("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";"));
        clubPlayers->setFrameShape(QFrame::Shape::Box);
        clubPlayers->setFrameShadow(QFrame::Shadow::Sunken);
        clubPlayers->setLineWidth(2);

        verticalLayout_4->addWidget(clubPlayers);

        clubSeason = new QLabel(layoutWidget1);
        clubSeason->setObjectName("clubSeason");
        clubSeason->setStyleSheet(QString::fromUtf8("color: rgb(85, 0, 255);\n"
"font: 700 11pt \"Segoe UI\";"));
        clubSeason->setFrameShape(QFrame::Shape::Box);
        clubSeason->setFrameShadow(QFrame::Shadow::Sunken);
        clubSeason->setLineWidth(2);

        verticalLayout_4->addWidget(clubSeason);

        playerActivityFrame = new QFrame(sessionFrame);
        playerActivityFrame->setObjectName("playerActivityFrame");
        playerActivityFrame->setGeometry(QRect(390, 20, 691, 241));
        playerActivityFrame->setFrameShape(QFrame::Shape::Panel);
        playerActivityFrame->setFrameShadow(QFrame::Shadow::Sunken);
        playerActivityFrame->setLineWidth(2);
        layoutWidget2 = new QWidget(playerActivityFrame);
        layoutWidget2->setObjectName("layoutWidget2");
        layoutWidget2->setGeometry(QRect(40, 20, 300, 201));
        verticalLayout_5 = new QVBoxLayout(layoutWidget2);
        verticalLayout_5->setObjectName("verticalLayout_5");
        verticalLayout_5->setContentsMargins(0, 0, 0, 0);
        playersF1ActivityLabel = new QLabel(layoutWidget2);
        playersF1ActivityLabel->setObjectName("playersF1ActivityLabel");

        verticalLayout_5->addWidget(playersF1ActivityLabel);

        playersF2ActivityLabel = new QLabel(layoutWidget2);
        playersF2ActivityLabel->setObjectName("playersF2ActivityLabel");

        verticalLayout_5->addWidget(playersF2ActivityLabel);

        playersF3ActivityLabel = new QLabel(layoutWidget2);
        playersF3ActivityLabel->setObjectName("playersF3ActivityLabel");

        verticalLayout_5->addWidget(playersF3ActivityLabel);

        playersF9ActivityLabel = new QLabel(layoutWidget2);
        playersF9ActivityLabel->setObjectName("playersF9ActivityLabel");

        verticalLayout_5->addWidget(playersF9ActivityLabel);

        playersF10ActivityLabel = new QLabel(layoutWidget2);
        playersF10ActivityLabel->setObjectName("playersF10ActivityLabel");

        verticalLayout_5->addWidget(playersF10ActivityLabel);

        playersEscActivityLabel = new QLabel(layoutWidget2);
        playersEscActivityLabel->setObjectName("playersEscActivityLabel");

        verticalLayout_5->addWidget(playersEscActivityLabel);

        playersDoubleClickActivityLabel = new QLabel(layoutWidget2);
        playersDoubleClickActivityLabel->setObjectName("playersDoubleClickActivityLabel");

        verticalLayout_5->addWidget(playersDoubleClickActivityLabel);

        clubFrameLabel = new QLabel(sessionFrame);
        clubFrameLabel->setObjectName("clubFrameLabel");
        clubFrameLabel->setGeometry(QRect(26, 9, 41, 20));
        clubFrameLabel->setStyleSheet(QString::fromUtf8("opacity : 255"));
        activityFrameLabel = new QLabel(sessionFrame);
        activityFrameLabel->setObjectName("activityFrameLabel");
        activityFrameLabel->setGeometry(QRect(402, 8, 63, 20));
        activityFrameLabel->setStyleSheet(QString::fromUtf8("opacity: 1.0;"));
        SessionFrameLabel = new QLabel(TopContainer);
        SessionFrameLabel->setObjectName("SessionFrameLabel");
        SessionFrameLabel->setGeometry(QRect(20, 10, 63, 20));
        SessionFrameLabel->setFont(font);
        playersTab = new QTabWidget(TopContainer);
        playersTab->setObjectName("playersTab");
        playersTab->setGeometry(QRect(20, 290, 1091, 571));
        playersTab->setAutoFillBackground(false);
        playersTab->setStyleSheet(QString::fromUtf8("background : rgb(236, 236, 236)"));
        PlayersTab = new QWidget();
        PlayersTab->setObjectName("PlayersTab");
        frame = new QFrame(PlayersTab);
        frame->setObjectName("frame");
        frame->setGeometry(QRect(10, 10, 341, 511));
        frame->setFrameShape(QFrame::Shape::Panel);
        frame->setFrameShadow(QFrame::Shadow::Raised);
        frame->setLineWidth(4);
        label = new QLabel(frame);
        label->setObjectName("label");
        label->setGeometry(QRect(32, 10, 131, 31));
        label->setFrameShape(QFrame::Shape::Box);
        label->setFrameShadow(QFrame::Shadow::Raised);
        label->setLineWidth(2);
        activePlayerLabel = new QLabel(frame);
        activePlayerLabel->setObjectName("activePlayerLabel");
        activePlayerLabel->setGeometry(QRect(40, 50, 81, 20));
        showAllPlayers = new QCheckBox(frame);
        showAllPlayers->setObjectName("showAllPlayers");
        showAllPlayers->setGeometry(QRect(140, 50, 87, 24));
        playersList = new QListWidget(frame);
        playersList->setObjectName("playersList");
        playersList->setGeometry(QRect(30, 80, 231, 411));
        playersList->setVerticalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAsNeeded);
        playersList->setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        playersList->setSelectionRectVisible(true);
        playersList->setSortingEnabled(false);
        newPlayerFrame = new QFrame(PlayersTab);
        newPlayerFrame->setObjectName("newPlayerFrame");
        newPlayerFrame->setGeometry(QRect(410, 10, 451, 501));
        newPlayerFrame->setFrameShape(QFrame::Shape::Panel);
        newPlayerFrame->setFrameShadow(QFrame::Shadow::Raised);
        newPlayerFrame->setLineWidth(2);
        newEditPlayerLabel = new QLabel(newPlayerFrame);
        newEditPlayerLabel->setObjectName("newEditPlayerLabel");
        newEditPlayerLabel->setGeometry(QRect(36, 15, 91, 31));
        newEditPlayerLabel->setFrameShape(QFrame::Shape::Box);
        newEditPlayerLabel->setFrameShadow(QFrame::Shadow::Raised);
        newEditPlayerLabel->setLineWidth(2);
        frame_3 = new QFrame(newPlayerFrame);
        frame_3->setObjectName("frame_3");
        frame_3->setGeometry(QRect(30, 55, 122, 431));
        frame_3->setFrameShape(QFrame::Shape::NoFrame);
        frame_3->setFrameShadow(QFrame::Shadow::Raised);
        frame_3->setLineWidth(2);
        formLayout = new QFormLayout(frame_3);
        formLayout->setObjectName("formLayout");
        formLayout->setVerticalSpacing(19);
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(14);
        verticalLayout->setObjectName("verticalLayout");
        firstNameLabel = new QLabel(frame_3);
        firstNameLabel->setObjectName("firstNameLabel");
        firstNameLabel->setEnabled(true);
        firstNameLabel->setAutoFillBackground(false);
        firstNameLabel->setScaledContents(false);
        firstNameLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(firstNameLabel);

        lastNameLabel = new QLabel(frame_3);
        lastNameLabel->setObjectName("lastNameLabel");
        lastNameLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(lastNameLabel);

        streetLabel = new QLabel(frame_3);
        streetLabel->setObjectName("streetLabel");
        streetLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(streetLabel);

        cityLabel = new QLabel(frame_3);
        cityLabel->setObjectName("cityLabel");
        cityLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(cityLabel);

        stateLabel = new QLabel(frame_3);
        stateLabel->setObjectName("stateLabel");
        stateLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(stateLabel);

        zipLabel = new QLabel(frame_3);
        zipLabel->setObjectName("zipLabel");
        zipLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(zipLabel);

        phoneLabel = new QLabel(frame_3);
        phoneLabel->setObjectName("phoneLabel");
        phoneLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(phoneLabel);

        emailLabel = new QLabel(frame_3);
        emailLabel->setObjectName("emailLabel");
        emailLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(emailLabel);

        accNumberLabel = new QLabel(frame_3);
        accNumberLabel->setObjectName("accNumberLabel");
        accNumberLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(accNumberLabel);

        expiresLabel = new QLabel(frame_3);
        expiresLabel->setObjectName("expiresLabel");
        expiresLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(expiresLabel);

        joinedLabel = new QLabel(frame_3);
        joinedLabel->setObjectName("joinedLabel");
        joinedLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(joinedLabel);

        activeLabel = new QLabel(frame_3);
        activeLabel->setObjectName("activeLabel");
        activeLabel->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        verticalLayout->addWidget(activeLabel);


        formLayout->setLayout(0, QFormLayout::LabelRole, verticalLayout);

        layoutWidget3 = new QWidget(newPlayerFrame);
        layoutWidget3->setObjectName("layoutWidget3");
        layoutWidget3->setGeometry(QRect(152, 61, 152, 421));
        verticalLayout_2 = new QVBoxLayout(layoutWidget3);
        verticalLayout_2->setSpacing(1);
        verticalLayout_2->setObjectName("verticalLayout_2");
        verticalLayout_2->setContentsMargins(9, 0, 0, 0);
        playerFirstNameEntry = new QLineEdit(layoutWidget3);
        playerFirstNameEntry->setObjectName("playerFirstNameEntry");

        verticalLayout_2->addWidget(playerFirstNameEntry);

        playerLastNameEntry = new QLineEdit(layoutWidget3);
        playerLastNameEntry->setObjectName("playerLastNameEntry");

        verticalLayout_2->addWidget(playerLastNameEntry);

        playerStreetEntry = new QLineEdit(layoutWidget3);
        playerStreetEntry->setObjectName("playerStreetEntry");

        verticalLayout_2->addWidget(playerStreetEntry);

        playerCityEntry = new QLineEdit(layoutWidget3);
        playerCityEntry->setObjectName("playerCityEntry");

        verticalLayout_2->addWidget(playerCityEntry);

        playerStateEntry = new QLineEdit(layoutWidget3);
        playerStateEntry->setObjectName("playerStateEntry");

        verticalLayout_2->addWidget(playerStateEntry);

        playerZipEntry = new QLineEdit(layoutWidget3);
        playerZipEntry->setObjectName("playerZipEntry");

        verticalLayout_2->addWidget(playerZipEntry);

        playerPhoneEntry = new QLineEdit(layoutWidget3);
        playerPhoneEntry->setObjectName("playerPhoneEntry");

        verticalLayout_2->addWidget(playerPhoneEntry);

        playerEmailEntry = new QLineEdit(layoutWidget3);
        playerEmailEntry->setObjectName("playerEmailEntry");

        verticalLayout_2->addWidget(playerEmailEntry);

        playerACCNumberEntry = new QLineEdit(layoutWidget3);
        playerACCNumberEntry->setObjectName("playerACCNumberEntry");

        verticalLayout_2->addWidget(playerACCNumberEntry);

        playerExpiresEntry = new QLineEdit(layoutWidget3);
        playerExpiresEntry->setObjectName("playerExpiresEntry");

        verticalLayout_2->addWidget(playerExpiresEntry);

        playerJoinedEntry = new QLineEdit(layoutWidget3);
        playerJoinedEntry->setObjectName("playerJoinedEntry");

        verticalLayout_2->addWidget(playerJoinedEntry);

        playerActiveEntry = new QLineEdit(layoutWidget3);
        playerActiveEntry->setObjectName("playerActiveEntry");

        verticalLayout_2->addWidget(playerActiveEntry);

        playersTab->addTab(PlayersTab, QString());
        tourneysTab = new QWidget();
        tourneysTab->setObjectName("tourneysTab");
        frame_2 = new QFrame(tourneysTab);
        frame_2->setObjectName("frame_2");
        frame_2->setGeometry(QRect(20, 10, 321, 51));
        frame_2->setFrameShape(QFrame::Shape::StyledPanel);
        frame_2->setFrameShadow(QFrame::Shadow::Plain);
        frame_2->setLineWidth(2);
        label_3 = new QLabel(frame_2);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(20, 10, 291, 31));
        label_3->setStyleSheet(QString::fromUtf8("color: rgb(68, 161, 28);\n"
"font: 700 12pt \"Segoe UI\";"));
        label_2 = new QLabel(tourneysTab);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(30, -1, 63, 20));
        frame_4 = new QFrame(tourneysTab);
        frame_4->setObjectName("frame_4");
        frame_4->setGeometry(QRect(20, 81, 311, 451));
        frame_4->setFrameShape(QFrame::Shape::Panel);
        frame_4->setFrameShadow(QFrame::Shadow::Sunken);
        frame_4->setLineWidth(2);
        existingTouneysList = new QListWidget(frame_4);
        existingTouneysList->setObjectName("existingTouneysList");
        existingTouneysList->setGeometry(QRect(20, 60, 231, 381));
        existingTouneysList->setLineWidth(2);
        layoutWidget4 = new QWidget(frame_4);
        layoutWidget4->setObjectName("layoutWidget4");
        layoutWidget4->setGeometry(QRect(20, 30, 221, 23));
        horizontalLayout = new QHBoxLayout(layoutWidget4);
        horizontalLayout->setObjectName("horizontalLayout");
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        label_6 = new QLabel(layoutWidget4);
        label_6->setObjectName("label_6");

        horizontalLayout->addWidget(label_6);

        label_5 = new QLabel(layoutWidget4);
        label_5->setObjectName("label_5");

        horizontalLayout->addWidget(label_5);

        label_7 = new QLabel(layoutWidget4);
        label_7->setObjectName("label_7");

        horizontalLayout->addWidget(label_7);

        label_4 = new QLabel(tourneysTab);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(30, 70, 141, 20));
        frame_5 = new QFrame(tourneysTab);
        frame_5->setObjectName("frame_5");
        frame_5->setGeometry(QRect(380, 10, 701, 501));
        frame_5->setFrameShape(QFrame::Shape::Panel);
        frame_5->setFrameShadow(QFrame::Shadow::Sunken);
        frame_5->setLineWidth(1);
        frame_6 = new QFrame(frame_5);
        frame_6->setObjectName("frame_6");
        frame_6->setGeometry(QRect(12, 20, 291, 91));
        frame_6->setFrameShape(QFrame::Shape::Panel);
        frame_6->setFrameShadow(QFrame::Shadow::Plain);
        frame_6->setLineWidth(1);
        label_9 = new QLabel(frame_6);
        label_9->setObjectName("label_9");
        label_9->setGeometry(QRect(20, 20, 221, 20));
        label_10 = new QLabel(frame_6);
        label_10->setObjectName("label_10");
        label_10->setGeometry(QRect(20, 50, 241, 20));
        frame_7 = new QFrame(frame_5);
        frame_7->setObjectName("frame_7");
        frame_7->setGeometry(QRect(10, 130, 331, 131));
        frame_7->setFrameShape(QFrame::Shape::Panel);
        frame_7->setFrameShadow(QFrame::Shadow::Plain);
        frame_7->setLineWidth(1);
        newTourneyNumberLabel = new QLabel(frame_7);
        newTourneyNumberLabel->setObjectName("newTourneyNumberLabel");
        newTourneyNumberLabel->setGeometry(QRect(20, 30, 151, 20));
        newTourneyDateLabel = new QLabel(frame_7);
        newTourneyDateLabel->setObjectName("newTourneyDateLabel");
        newTourneyDateLabel->setGeometry(QRect(20, 80, 141, 20));
        newTourneNumber = new QLineEdit(frame_7);
        newTourneNumber->setObjectName("newTourneNumber");
        newTourneNumber->setGeometry(QRect(190, 30, 51, 26));
        newTourneNumber->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        newTourneyDate = new QLineEdit(frame_7);
        newTourneyDate->setObjectName("newTourneyDate");
        newTourneyDate->setGeometry(QRect(190, 80, 113, 26));
        newTourneyDate->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        newTourneyLabel = new QLabel(frame_5);
        newTourneyLabel->setObjectName("newTourneyLabel");
        newTourneyLabel->setGeometry(QRect(40, 120, 101, 20));
        createTourneyLabel = new QLabel(tourneysTab);
        createTourneyLabel->setObjectName("createTourneyLabel");
        createTourneyLabel->setGeometry(QRect(400, 0, 131, 20));
        playersTab->addTab(tourneysTab, QString());
        resultsTab = new QWidget();
        resultsTab->setObjectName("resultsTab");
        frame_8 = new QFrame(resultsTab);
        frame_8->setObjectName("frame_8");
        frame_8->setGeometry(QRect(10, 10, 1071, 541));
        frame_8->setFrameShape(QFrame::Shape::Panel);
        frame_8->setFrameShadow(QFrame::Shadow::Sunken);
        frame_8->setLineWidth(2);
        frame_9 = new QFrame(frame_8);
        frame_9->setObjectName("frame_9");
        frame_9->setGeometry(QRect(20, 20, 221, 101));
        frame_9->setFrameShape(QFrame::Shape::Panel);
        frame_9->setFrameShadow(QFrame::Shadow::Raised);
        frame_9->setLineWidth(2);
        resultsTouneyDateLabel = new QLabel(frame_9);
        resultsTouneyDateLabel->setObjectName("resultsTouneyDateLabel");
        resultsTouneyDateLabel->setGeometry(QRect(10, 10, 101, 20));
        resultsTounryNumberLabel = new QLabel(frame_9);
        resultsTounryNumberLabel->setObjectName("resultsTounryNumberLabel");
        resultsTounryNumberLabel->setGeometry(QRect(10, 40, 91, 20));
        resultsTourneyCountLabel = new QLabel(frame_9);
        resultsTourneyCountLabel->setObjectName("resultsTourneyCountLabel");
        resultsTourneyCountLabel->setGeometry(QRect(10, 70, 63, 20));
        resultsTourneyDate = new QLabel(frame_9);
        resultsTourneyDate->setObjectName("resultsTourneyDate");
        resultsTourneyDate->setGeometry(QRect(120, 10, 91, 20));
        resultsTourneyDate->setStyleSheet(QString::fromUtf8("background :rgb(255, 255, 255)\n"
""));
        resultsTourneyNumber = new QLabel(frame_9);
        resultsTourneyNumber->setObjectName("resultsTourneyNumber");
        resultsTourneyNumber->setGeometry(QRect(120, 40, 51, 20));
        resultsTourneyNumber->setStyleSheet(QString::fromUtf8("background:rgb(255, 255, 255)"));
        resultsTourneyCount = new QLabel(frame_9);
        resultsTourneyCount->setObjectName("resultsTourneyCount");
        resultsTourneyCount->setGeometry(QRect(120, 70, 51, 20));
        resultsTourneyCount->setStyleSheet(QString::fromUtf8("background:rgb(255, 255, 255)"));
        frame_10 = new QFrame(frame_8);
        frame_10->setObjectName("frame_10");
        frame_10->setGeometry(QRect(260, 20, 241, 101));
        frame_10->setFrameShape(QFrame::Shape::Panel);
        frame_10->setFrameShadow(QFrame::Shadow::Raised);
        frame_10->setLineWidth(2);
        label_27 = new QLabel(frame_10);
        label_27->setObjectName("label_27");
        label_27->setGeometry(QRect(89, 10, 31, 20));
        label_28 = new QLabel(frame_10);
        label_28->setObjectName("label_28");
        label_28->setGeometry(QRect(130, 10, 51, 20));
        label_29 = new QLabel(frame_10);
        label_29->setObjectName("label_29");
        label_29->setGeometry(QRect(187, 10, 31, 20));
        label_30 = new QLabel(frame_10);
        label_30->setObjectName("label_30");
        label_30->setGeometry(QRect(10, 40, 63, 20));
        label_31 = new QLabel(frame_10);
        label_31->setObjectName("label_31");
        label_31->setGeometry(QRect(10, 70, 63, 20));
        resultsSpreadPlus = new QLabel(frame_10);
        resultsSpreadPlus->setObjectName("resultsSpreadPlus");
        resultsSpreadPlus->setGeometry(QRect(80, 40, 41, 20));
        resultsSpreadPlus->setStyleSheet(QString::fromUtf8("background: rgb(220, 255, 228);\n"
"\n"
""));
        resultsSpreadMinus = new QLabel(frame_10);
        resultsSpreadMinus->setObjectName("resultsSpreadMinus");
        resultsSpreadMinus->setGeometry(QRect(130, 40, 41, 20));
        resultsSpreadMinus->setStyleSheet(QString::fromUtf8("background: rgb(255, 204, 202)"));
        resultsSpreadDiff = new QLabel(frame_10);
        resultsSpreadDiff->setObjectName("resultsSpreadDiff");
        resultsSpreadDiff->setGeometry(QRect(180, 40, 51, 20));
        resultsSpreadDiff->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        resultsSkunksPlus = new QLabel(frame_10);
        resultsSkunksPlus->setObjectName("resultsSkunksPlus");
        resultsSkunksPlus->setGeometry(QRect(80, 70, 41, 20));
        resultsSkunksPlus->setStyleSheet(QString::fromUtf8("background: rgb(220, 255, 228);\n"
"\n"
""));
        resultsSpreadMinus_2 = new QLabel(frame_10);
        resultsSpreadMinus_2->setObjectName("resultsSpreadMinus_2");
        resultsSpreadMinus_2->setGeometry(QRect(130, 70, 41, 20));
        resultsSpreadMinus_2->setStyleSheet(QString::fromUtf8("background:rgb(255, 219, 219)"));
        resultsSkunksDiff = new QLabel(frame_10);
        resultsSkunksDiff->setObjectName("resultsSkunksDiff");
        resultsSkunksDiff->setGeometry(QRect(180, 70, 41, 20));
        resultsSkunksDiff->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        frame_11 = new QFrame(frame_8);
        frame_11->setObjectName("frame_11");
        frame_11->setGeometry(QRect(20, 140, 221, 381));
        frame_11->setFrameShape(QFrame::Shape::Panel);
        frame_11->setFrameShadow(QFrame::Shadow::Sunken);
        frame_11->setLineWidth(2);
        resultsPlayList = new QListWidget(frame_11);
        resultsPlayList->setObjectName("resultsPlayList");
        resultsPlayList->setGeometry(QRect(10, 50, 181, 331));
        resultsPointsLabel = new QLabel(frame_11);
        resultsPointsLabel->setObjectName("resultsPointsLabel");
        resultsPointsLabel->setGeometry(QRect(20, 20, 41, 20));
        resultsPlayerNameLabel_2 = new QLabel(frame_11);
        resultsPlayerNameLabel_2->setObjectName("resultsPlayerNameLabel_2");
        resultsPlayerNameLabel_2->setGeometry(QRect(99, 22, 51, 20));
        frame_12 = new QFrame(frame_8);
        frame_12->setObjectName("frame_12");
        frame_12->setGeometry(QRect(260, 140, 351, 381));
        frame_12->setFrameShape(QFrame::Shape::Panel);
        frame_12->setFrameShadow(QFrame::Shadow::Sunken);
        resultsPlayerNameLabel = new QLabel(frame_12);
        resultsPlayerNameLabel->setObjectName("resultsPlayerNameLabel");
        resultsPlayerNameLabel->setGeometry(QRect(20, 20, 71, 20));
        resultsPlayerNameLabel->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_42 = new QLabel(frame_12);
        label_42->setObjectName("label_42");
        label_42->setGeometry(QRect(160, 20, 31, 20));
        label_43 = new QLabel(frame_12);
        label_43->setObjectName("label_43");
        label_43->setGeometry(QRect(190, 20, 31, 20));
        label_44 = new QLabel(frame_12);
        label_44->setObjectName("label_44");
        label_44->setGeometry(QRect(230, 20, 31, 20));
        label_45 = new QLabel(frame_12);
        label_45->setObjectName("label_45");
        label_45->setGeometry(QRect(270, 20, 31, 20));
        label_46 = new QLabel(frame_12);
        label_46->setObjectName("label_46");
        label_46->setGeometry(QRect(300, 20, 31, 20));
        tourneyResultsList = new QListWidget(frame_12);
        tourneyResultsList->setObjectName("tourneyResultsList");
        tourneyResultsList->setGeometry(QRect(30, 50, 301, 321));
        frame_13 = new QFrame(frame_8);
        frame_13->setObjectName("frame_13");
        frame_13->setGeometry(QRect(510, 20, 551, 101));
        frame_13->setFrameShape(QFrame::Shape::Panel);
        frame_13->setFrameShadow(QFrame::Shadow::Raised);
        frame_13->setLineWidth(2);
        resultPlayerNameLabel = new QLabel(frame_13);
        resultPlayerNameLabel->setObjectName("resultPlayerNameLabel");
        resultPlayerNameLabel->setGeometry(QRect(10, 10, 151, 20));
        resultPlayerNameLabel->setAlignment(Qt::AlignmentFlag::AlignCenter);
        resultsPlayerName = new QLabel(frame_13);
        resultsPlayerName->setObjectName("resultsPlayerName");
        resultsPlayerName->setGeometry(QRect(22, 50, 171, 20));
        resultPlayerGp = new QLineEdit(frame_13);
        resultPlayerGp->setObjectName("resultPlayerGp");
        resultPlayerGp->setGeometry(QRect(201, 50, 31, 26));
        resultPlayerGp->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        resutlPlayerGw = new QLineEdit(frame_13);
        resutlPlayerGw->setObjectName("resutlPlayerGw");
        resutlPlayerGw->setGeometry(QRect(250, 50, 31, 26));
        resutlPlayerGw->setStyleSheet(QString::fromUtf8("background:rgb(255, 255, 255)"));
        resultPlayerSprd = new QLineEdit(frame_13);
        resultPlayerSprd->setObjectName("resultPlayerSprd");
        resultPlayerSprd->setGeometry(QRect(300, 50, 51, 26));
        resultPlayerSprd->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        resultPlayerTkn = new QLineEdit(frame_13);
        resultPlayerTkn->setObjectName("resultPlayerTkn");
        resultPlayerTkn->setGeometry(QRect(370, 50, 31, 26));
        resultPlayerTkn->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        resultPlayerDollars = new QLineEdit(frame_13);
        resultPlayerDollars->setObjectName("resultPlayerDollars");
        resultPlayerDollars->setGeometry(QRect(420, 50, 31, 26));
        resultPlayerDollars->setStyleSheet(QString::fromUtf8("background: rgb(255, 255, 255)"));
        resultPlayerGiven = new QLineEdit(frame_13);
        resultPlayerGiven->setObjectName("resultPlayerGiven");
        resultPlayerGiven->setEnabled(false);
        resultPlayerGiven->setGeometry(QRect(470, 50, 31, 26));
        resultPlayerGiven->setStyleSheet(QString::fromUtf8("background: rgb(236, 236, 236)"));
        layoutWidget5 = new QWidget(frame_13);
        layoutWidget5->setObjectName("layoutWidget5");
        layoutWidget5->setGeometry(QRect(200, 10, 321, 23));
        horizontalLayout_2 = new QHBoxLayout(layoutWidget5);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        resultGpLabel = new QLabel(layoutWidget5);
        resultGpLabel->setObjectName("resultGpLabel");

        horizontalLayout_2->addWidget(resultGpLabel);

        resultGwLabel = new QLabel(layoutWidget5);
        resultGwLabel->setObjectName("resultGwLabel");

        horizontalLayout_2->addWidget(resultGwLabel);

        resultSprdLabel = new QLabel(layoutWidget5);
        resultSprdLabel->setObjectName("resultSprdLabel");

        horizontalLayout_2->addWidget(resultSprdLabel);

        resultTknLabel = new QLabel(layoutWidget5);
        resultTknLabel->setObjectName("resultTknLabel");

        horizontalLayout_2->addWidget(resultTknLabel);

        resultDollarLabel = new QLabel(layoutWidget5);
        resultDollarLabel->setObjectName("resultDollarLabel");

        horizontalLayout_2->addWidget(resultDollarLabel);

        resultGvnLabel = new QLabel(layoutWidget5);
        resultGvnLabel->setObjectName("resultGvnLabel");

        horizontalLayout_2->addWidget(resultGvnLabel);

        label_40 = new QLabel(frame_8);
        label_40->setObjectName("label_40");
        label_40->setGeometry(QRect(270, 130, 111, 20));
        label_14 = new QLabel(resultsTab);
        label_14->setObjectName("label_14");
        label_14->setGeometry(QRect(20, 0, 101, 20));
        playersTab->addTab(resultsTab, QString());
        reportsTab = new QWidget();
        reportsTab->setObjectName("reportsTab");
        frame_14 = new QFrame(reportsTab);
        frame_14->setObjectName("frame_14");
        frame_14->setGeometry(QRect(20, 31, 191, 491));
        frame_14->setFrameShape(QFrame::Shape::Panel);
        frame_14->setFrameShadow(QFrame::Shadow::Sunken);
        frame_14->setLineWidth(2);
        tourneysList = new QListWidget(frame_14);
        tourneysList->setObjectName("tourneysList");
        tourneysList->setGeometry(QRect(10, 20, 151, 471));
        frame_15 = new QFrame(reportsTab);
        frame_15->setObjectName("frame_15");
        frame_15->setGeometry(QRect(250, 30, 251, 501));
        frame_15->setFrameShape(QFrame::Shape::Panel);
        frame_15->setFrameShadow(QFrame::Shadow::Sunken);
        frame_15->setLineWidth(2);
        checkBox = new QCheckBox(frame_15);
        checkBox->setObjectName("checkBox");
        checkBox->setGeometry(QRect(20, 20, 101, 24));
        pushButton = new QPushButton(frame_15);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(60, 390, 121, 41));
        layoutWidget6 = new QWidget(frame_15);
        layoutWidget6->setObjectName("layoutWidget6");
        layoutWidget6->setGeometry(QRect(20, 80, 193, 275));
        verticalLayout_6 = new QVBoxLayout(layoutWidget6);
        verticalLayout_6->setObjectName("verticalLayout_6");
        verticalLayout_6->setContentsMargins(0, 0, 0, 0);
        checkBox_2 = new QCheckBox(layoutWidget6);
        checkBox_2->setObjectName("checkBox_2");

        verticalLayout_6->addWidget(checkBox_2);

        checkBox_3 = new QCheckBox(layoutWidget6);
        checkBox_3->setObjectName("checkBox_3");

        verticalLayout_6->addWidget(checkBox_3);

        checkBox_4 = new QCheckBox(layoutWidget6);
        checkBox_4->setObjectName("checkBox_4");

        verticalLayout_6->addWidget(checkBox_4);

        checkBox_5 = new QCheckBox(layoutWidget6);
        checkBox_5->setObjectName("checkBox_5");

        verticalLayout_6->addWidget(checkBox_5);

        checkBox_6 = new QCheckBox(layoutWidget6);
        checkBox_6->setObjectName("checkBox_6");

        verticalLayout_6->addWidget(checkBox_6);

        checkBox_8 = new QCheckBox(layoutWidget6);
        checkBox_8->setObjectName("checkBox_8");

        verticalLayout_6->addWidget(checkBox_8);

        checkBox_7 = new QCheckBox(layoutWidget6);
        checkBox_7->setObjectName("checkBox_7");

        verticalLayout_6->addWidget(checkBox_7);

        checkBox_9 = new QCheckBox(layoutWidget6);
        checkBox_9->setObjectName("checkBox_9");

        verticalLayout_6->addWidget(checkBox_9);

        checkBox_10 = new QCheckBox(layoutWidget6);
        checkBox_10->setObjectName("checkBox_10");

        verticalLayout_6->addWidget(checkBox_10);

        label_23 = new QLabel(reportsTab);
        label_23->setObjectName("label_23");
        label_23->setGeometry(QRect(30, 18, 63, 20));
        label_24 = new QLabel(reportsTab);
        label_24->setObjectName("label_24");
        label_24->setGeometry(QRect(260, 20, 63, 20));
        playersTab->addTab(reportsTab, QString());
        frame_15->raise();
        frame_14->raise();
        label_23->raise();
        label_24->raise();
        Master->setCentralWidget(TopContainer);

        retranslateUi(Master);

        playersTab->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(Master);
    } // setupUi

    void retranslateUi(QMainWindow *Master)
    {
        Master->setWindowTitle(QCoreApplication::translate("Master", "Cribbage Grass Roots", nullptr));
        clubNumberLabel->setText(QCoreApplication::translate("Master", "Club Number:", nullptr));
        clubNameLabel->setText(QCoreApplication::translate("Master", "Club Name:", nullptr));
        clubPlayersLabel->setText(QCoreApplication::translate("Master", "Players in Club:", nullptr));
        clubSeasonLabel->setText(QCoreApplication::translate("Master", "Season:", nullptr));
        clubNumber->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        clubName->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        clubPlayers->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        clubSeason->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        playersF1ActivityLabel->setText(QCoreApplication::translate("Master", "F1    Get help with this activity", nullptr));
        playersF2ActivityLabel->setText(QCoreApplication::translate("Master", "F2    Edit player selected in listbox", nullptr));
        playersF3ActivityLabel->setText(QCoreApplication::translate("Master", "F3    Create a new player", nullptr));
        playersF9ActivityLabel->setText(QCoreApplication::translate("Master", "F9    Toggle active status for selected player", nullptr));
        playersF10ActivityLabel->setText(QCoreApplication::translate("Master", "F10  Save all current changes", nullptr));
        playersEscActivityLabel->setText(QCoreApplication::translate("Master", "Esc   Quit current activity", nullptr));
        playersDoubleClickActivityLabel->setText(QCoreApplication::translate("Master", "Double Click entry to toggle active status", nullptr));
        clubFrameLabel->setText(QCoreApplication::translate("Master", "Club", nullptr));
        activityFrameLabel->setText(QCoreApplication::translate("Master", "Activity", nullptr));
        SessionFrameLabel->setText(QCoreApplication::translate("Master", "Session", nullptr));
        label->setText(QCoreApplication::translate("Master", "Existing Players", nullptr));
        activePlayerLabel->setText(QCoreApplication::translate("Master", "* = Active", nullptr));
        showAllPlayers->setText(QCoreApplication::translate("Master", "Show All", nullptr));
        newEditPlayerLabel->setText(QCoreApplication::translate("Master", "New Player", nullptr));
        firstNameLabel->setText(QCoreApplication::translate("Master", "First Name: ", nullptr));
        lastNameLabel->setText(QCoreApplication::translate("Master", "Last Name: ", nullptr));
        streetLabel->setText(QCoreApplication::translate("Master", "Street: ", nullptr));
        cityLabel->setText(QCoreApplication::translate("Master", "City: ", nullptr));
        stateLabel->setText(QCoreApplication::translate("Master", "State: ", nullptr));
        zipLabel->setText(QCoreApplication::translate("Master", "Zip: ", nullptr));
        phoneLabel->setText(QCoreApplication::translate("Master", "Phone: ", nullptr));
        emailLabel->setText(QCoreApplication::translate("Master", "Email: ", nullptr));
        accNumberLabel->setText(QCoreApplication::translate("Master", "Acc Numb: ", nullptr));
        expiresLabel->setText(QCoreApplication::translate("Master", "Expires: ", nullptr));
        joinedLabel->setText(QCoreApplication::translate("Master", "Joined: ", nullptr));
        activeLabel->setText(QCoreApplication::translate("Master", "Active: ", nullptr));
        playersTab->setTabText(playersTab->indexOf(PlayersTab), QCoreApplication::translate("Master", "Players", nullptr));
        label_3->setText(QCoreApplication::translate("Master", "F6 - Enter results for selected tourney", nullptr));
        label_2->setText(QCoreApplication::translate("Master", "Tourneys", nullptr));
        label_6->setText(QCoreApplication::translate("Master", "No.", nullptr));
        label_5->setText(QCoreApplication::translate("Master", "Data", nullptr));
        label_7->setText(QCoreApplication::translate("Master", "Date", nullptr));
        label_4->setText(QCoreApplication::translate("Master", "Existing Tournaments", nullptr));
        label_9->setText(QCoreApplication::translate("Master", "Enter new fields", nullptr));
        label_10->setText(QCoreApplication::translate("Master", "Then F10 to save or Esc to cancel", nullptr));
        newTourneyNumberLabel->setText(QCoreApplication::translate("Master", "New Tourney Number:", nullptr));
        newTourneyDateLabel->setText(QCoreApplication::translate("Master", "New Tourney Date", nullptr));
        newTourneyLabel->setText(QCoreApplication::translate("Master", "New Tourney", nullptr));
        createTourneyLabel->setText(QCoreApplication::translate("Master", "Create a Tourney", nullptr));
        playersTab->setTabText(playersTab->indexOf(tourneysTab), QCoreApplication::translate("Master", "Tourneys", nullptr));
        resultsTouneyDateLabel->setText(QCoreApplication::translate("Master", "Tourney Date:", nullptr));
        resultsTounryNumberLabel->setText(QCoreApplication::translate("Master", "Tourney No.", nullptr));
        resultsTourneyCountLabel->setText(QCoreApplication::translate("Master", "Count:", nullptr));
        resultsTourneyDate->setText(QCoreApplication::translate("Master", "date", nullptr));
        resultsTourneyNumber->setText(QCoreApplication::translate("Master", "no.", nullptr));
        resultsTourneyCount->setText(QCoreApplication::translate("Master", "count", nullptr));
        label_27->setText(QCoreApplication::translate("Master", "Plus", nullptr));
        label_28->setText(QCoreApplication::translate("Master", "Minus", nullptr));
        label_29->setText(QCoreApplication::translate("Master", "Diff", nullptr));
        label_30->setText(QCoreApplication::translate("Master", "Spread", nullptr));
        label_31->setText(QCoreApplication::translate("Master", "Skunks", nullptr));
        resultsSpreadPlus->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultsSpreadMinus->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultsSpreadDiff->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultsSkunksPlus->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultsSpreadMinus_2->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultsSkunksDiff->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultsPointsLabel->setText(QCoreApplication::translate("Master", "Points", nullptr));
        resultsPlayerNameLabel_2->setText(QCoreApplication::translate("Master", "Player", nullptr));
        resultsPlayerNameLabel->setText(QCoreApplication::translate("Master", "Name", nullptr));
        label_42->setText(QCoreApplication::translate("Master", "GP", nullptr));
        label_43->setText(QCoreApplication::translate("Master", "GW", nullptr));
        label_44->setText(QCoreApplication::translate("Master", "Sprd", nullptr));
        label_45->setText(QCoreApplication::translate("Master", "Tkn", nullptr));
        label_46->setText(QCoreApplication::translate("Master", "Gvn", nullptr));
        resultPlayerNameLabel->setText(QCoreApplication::translate("Master", "Name", nullptr));
        resultsPlayerName->setText(QCoreApplication::translate("Master", "TextLabel", nullptr));
        resultGpLabel->setText(QCoreApplication::translate("Master", "GP", nullptr));
        resultGwLabel->setText(QCoreApplication::translate("Master", "GW", nullptr));
        resultSprdLabel->setText(QCoreApplication::translate("Master", "SPRD", nullptr));
        resultTknLabel->setText(QCoreApplication::translate("Master", "TKN", nullptr));
        resultDollarLabel->setText(QCoreApplication::translate("Master", "$'s", nullptr));
        resultGvnLabel->setText(QCoreApplication::translate("Master", "GVN", nullptr));
        label_40->setText(QCoreApplication::translate("Master", "Tourney Results", nullptr));
        label_14->setText(QCoreApplication::translate("Master", "Results Panel", nullptr));
        playersTab->setTabText(playersTab->indexOf(resultsTab), QCoreApplication::translate("Master", "Results", nullptr));
        checkBox->setText(QCoreApplication::translate("Master", "All Reports", nullptr));
        pushButton->setText(QCoreApplication::translate("Master", "Run Reports", nullptr));
        checkBox_2->setText(QCoreApplication::translate("Master", "Alpha Report", nullptr));
        checkBox_3->setText(QCoreApplication::translate("Master", "Batting Averages Report", nullptr));
        checkBox_4->setText(QCoreApplication::translate("Master", "Cash Report", nullptr));
        checkBox_5->setText(QCoreApplication::translate("Master", "Individ. Stats Report", nullptr));
        checkBox_6->setText(QCoreApplication::translate("Master", "National Avges Report", nullptr));
        checkBox_8->setText(QCoreApplication::translate("Master", "Qtr. Drop Report", nullptr));
        checkBox_7->setText(QCoreApplication::translate("Master", "Qtr. Full Report", nullptr));
        checkBox_9->setText(QCoreApplication::translate("Master", "Skunk Report", nullptr));
        checkBox_10->setText(QCoreApplication::translate("Master", "Tourney Report", nullptr));
        label_23->setText(QCoreApplication::translate("Master", "Tourneys", nullptr));
        label_24->setText(QCoreApplication::translate("Master", "Reports", nullptr));
        playersTab->setTabText(playersTab->indexOf(reportsTab), QCoreApplication::translate("Master", "Reports", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Master: public Ui_Master {};
} // namespace Ui

QT_END_NAMESPACE

#endif // CRIBBAGEV1_H
