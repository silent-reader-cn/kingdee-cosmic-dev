# 采委会决策单号-src_decisionbillnotwo

## 采委会决策单号-主表 t_src_decide

- **表名称：** 采委会决策单号-主表
- **表名：** t_src_decide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fdecisionamount | 采委会剩余金额 | numeric | 23 | 10 | √ | 0 | 采委会剩余金额 |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmulilangtextfield | fmulilangtextfield | varchar | 300 |  | √ | ' ' |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fdecisionform | fdecisionform | int8 | 64 |  | √ | 0 |  |
| 7 | ftitle | 标题 | varchar | 300 |  | √ | ' ' | 标题 |
| 8 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fpurgroup | fpurgroup | int8 | 64 |  | √ | 0 |  |
| 10 | fdecidecontent | fdecidecontent | varchar | 255 |  | √ | ' ' |  |
| 11 | fsourcebillno | fsourcebillno | varchar | 100 |  | √ | ' ' |  |
| 12 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 13 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 14 | ftemplate | ftemplate | int8 | 64 |  | √ | 0 |  |
| 15 | fstartvetodate | fstartvetodate | timestamp | 0 |  |  | null |  |
| 16 | fischanging | fischanging | varchar | 30 |  | √ | '0' |  |
| 17 | fpurdept | fpurdept | int8 | 64 |  | √ | 0 |  |
| 18 | fisfunction | 生效状态 | varchar | 30 |  | √ | '0' | 生效状态,枚举: A :未生效 B :生效 C :失效 D :过期 |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :投票中 C :投票完成 D :投票中止 E :审核中 F :审核通过 |
| 20 | forgids | forgids | text | 0 |  |  | ' ' |  |
| 21 | fdecidetime | 决策时间 | timestamp | 0 |  |  | null | 决策时间 |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 24 | findicate | findicate | varchar | 30 |  | √ | ' ' |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fstage | fstage | varchar | 30 |  | √ | ' ' |  |
| 27 | fscoreropinion | fscoreropinion | varchar | 255 |  | √ | ' ' |  |
| 28 | fdemandaffiliateid | fdemandaffiliateid | int8 | 64 |  | √ | 0 |  |
| 29 | fbizstatus | 投票是否通过 | bpchar | 1 |  | √ | ' ' | 投票是否通过,枚举: A :待确认 B :通过 C :未通过 |
| 30 | freviewdate | freviewdate | timestamp | 0 |  |  | null |  |
| 31 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | fisfinal | fisfinal | bpchar | 1 |  | √ | '0' |  |
| 34 | fregion | fregion | int8 | 64 |  | √ | 0 |  |
| 35 | flastdecision | flastdecision | int8 | 64 |  | √ | 0 |  |
| 36 | fmeetingcontent | fmeetingcontent | varchar | 255 |  | √ | ' ' |  |
| 37 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 38 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 39 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 40 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 41 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 42 | fcostattribution | fcostattribution | int8 | 64 |  | √ | 0 |  |
| 43 | fcencortype | fcencortype | varchar | 30 |  | √ | ' ' |  |
| 44 | fdecisiontype | 决策类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 45 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 46 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 47 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 48 | fisqualify | fisqualify | bpchar | 1 |  | √ | '0' |  |
| 49 | fnotifychairmandate | fnotifychairmandate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_decide |  | fid |
| 2 | idx_src_decide_fbillno |  | fbillno |
| 3 | idx_src_decide_fbillstatus |  | fbillstatus |
| 4 | idx_src_decide_fdecisiontype |  | fdecisiontype |
| 5 | idx_src_decide_fisfunction |  | fisfunction |

---

## 采购组织-多选基础资料表 t_src_decision_purorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_decision_purorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decision_purorg_fid |  | fid |
| 2 | pk_src_decision_purorg |  | fpkid |
| 3 | idx_src_decision_purorg_bid |  | fbasedataid |

---

## 采委会决策单号-多语言表 t_src_decide_l

- **表名称：** 采委会决策单号-多语言表
- **表名：** t_src_decide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 300 |  | √ | ' ' | 标题 |
| 3 | fmulilangtextfield | fmulilangtextfield | varchar | 300 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decide_l_ftitle |  | ftitle |
| 2 | pk_src_decide_l |  | fpkid |

---

## 单据体-子表 t_src_decisionscene

- **表名称：** 单据体-子表
- **表名：** t_src_decisionscene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherruleassess | fotherruleassess | varchar | 1000 |  | √ | ' ' |  |
| 3 | fsceneno_des | fsceneno_des | varchar | 100 |  | √ | ' ' |  |
| 4 | fsceneamount | fsceneamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fotherreason | fotherreason | varchar | 255 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fbargainrule | fbargainrule | varchar | 30 |  | √ | ' ' |  |
| 9 | fsuppliernum | fsuppliernum | int8 | 64 |  | √ | 0 |  |
| 10 | ftitle | ftitle | varchar | 50 |  | √ | ' ' |  |
| 11 | frange | frange | varchar | 50 |  | √ | ' ' |  |
| 12 | fscenestatus | fscenestatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fchassisttypeid | fchassisttypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fprojectno | fprojectno | varchar | 50 |  | √ | ' ' |  |
| 15 | fdetailid | fdetailid | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | fbillno | varchar | 100 |  | √ | ' ' |  |
| 17 | fwinrule | fwinrule | int8 | 64 |  | √ | 0 |  |
| 18 | fisfunction | fisfunction | bpchar | 1 |  | √ | '0' |  |
| 19 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbillno2 | fbillno2 | varchar | 50 |  | √ | ' ' |  |
| 22 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fscenename_des | fscenename_des | varchar | 100 |  | √ | ' ' |  |
| 25 | fpurtype | fpurtype | int8 | 64 |  | √ | 0 |  |
| 26 | fruleassess | fruleassess | varchar | 30 |  | √ | ' ' |  |
| 27 | fquerycondition | fquerycondition | varchar | 255 |  | √ | ' ' |  |
| 28 | fscenechasisstid | fscenechasisstid | int8 | 64 |  | √ | 0 |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fotherwinrule | fotherwinrule | varchar | 1000 |  | √ | ' ' |  |
| 32 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 33 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 34 | fseq1 | 场景编号 | varchar | 50 |  | √ | ' ' | 场景编号 |
| 35 | fcompreper | fcompreper | numeric | 23 | 10 | √ | 0 |  |
| 36 | fwinrule2 | fwinrule2 | int8 | 64 |  | √ | 0 |  |
| 37 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 38 | fbiztype | fbiztype | varchar | 30 |  | √ | ' ' |  |
| 39 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 40 | faftertalkrule | faftertalkrule | varchar | 1000 |  | √ | ' ' |  |
| 41 | fsolereason | fsolereason | varchar | 100 |  | √ | ' ' |  |
| 42 | forderrule | forderrule | varchar | 1000 |  | √ | ' ' |  |
| 43 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | ftalkrule | ftalkrule | int8 | 64 |  | √ | 0 |  |
| 46 | fskillper | fskillper | numeric | 23 | 10 | √ | 0 |  |
| 47 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 48 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 49 | fbusinessper | fbusinessper | numeric | 23 | 10 | √ | 0 |  |
| 50 | fisprice | fisprice | bpchar | 1 |  | √ | '0' |  |
| 51 | fsrcflowconfig | fsrcflowconfig | int8 | 64 |  | √ | 0 |  |
| 52 | fdiscardrule | fdiscardrule | varchar | 1000 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_deciscene_pid |  | fprojectid |
| 2 | pk_src_decisionscene |  | fentryid |
| 3 | idx_src_deciscene_fid |  | fid |
