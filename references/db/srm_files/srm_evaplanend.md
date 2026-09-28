# 评估计划终止-srm_evaplanend

## 评估计划终止-主表 t_pur_evaplan

- **表名称：** 评估计划终止-主表
- **表名：** t_pur_evaplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fistypescorer | fistypescorer | bpchar | 1 |  | √ | ' ' |  |
| 3 | fevamethod | fevamethod | bpchar | 1 |  | √ | 'A' |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fbizstatus | 计划状态 | bpchar | 1 |  | √ | ' ' | 计划状态,枚举: Z :已终止 |
| 7 | fbilldate | 评估日期 | timestamp | 0 |  |  | null | 评估日期 |
| 8 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fdatetimeto | fdatetimeto | timestamp | 0 |  |  | null |  |
| 10 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 11 | fdatefrom | fdatefrom | timestamp | 0 |  |  | null |  |
| 12 | fgroupevaplannoid | fgroupevaplannoid | int8 | 64 |  | √ | 0 |  |
| 13 | fbillno | 计划单号 | varchar | 80 |  | √ | ' ' | 计划单号 |
| 14 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 15 | fname | 计划名称 | varchar | 100 |  | √ | ' ' | 计划名称 |
| 16 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 17 | fgradeid | fgradeid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 19 | fevatypeid | fevatypeid | int8 | 64 |  | √ | 0 |  |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 22 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 23 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 24 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 25 | fdatetimefrom | fdatetimefrom | timestamp | 0 |  |  | null |  |
| 26 | fperiod | fperiod | bpchar | 1 |  | √ | ' ' |  |
| 27 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_evaplan_fbillno |  | fbillno |
| 2 | idx_pur_evaplan_fbilldate |  | fbilldate |
| 3 | t_pur_evaplan_pkey |  | fid |

---

## 评估计划终止-分表 t_pur_evaplan_a

- **表名称：** 评估计划终止-分表
- **表名：** t_pur_evaplan_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 6 | fterminatedate | 终止时间 | timestamp | 0 |  |  | null | 终止时间 |
| 7 | fpushnotice | fpushnotice | bpchar | 1 |  | √ | '0' |  |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 10 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 13 | ftermination | 终止意见 | varchar | 255 |  | √ | ' ' | 终止意见 |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fterminaterid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpushscore | fpushscore | bpchar | 1 |  | √ | '0' |  |
| 17 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 18 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_evaplan_a_pkey |  | fid |
| 2 | idx_pur_evaplan_a_ftime |  | fcreatetime |

---

## 评估计划终止-多语言表 t_pur_evaplan_l

- **表名称：** 评估计划终止-多语言表
- **表名：** t_pur_evaplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 3 | fname | 计划名称 | varchar | 100 |  | √ | ' ' | 计划名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_evaplan_l_pkey |  | fpkid |
| 2 | idx_pur_evaplan_l_fid |  | fid,flocaleid |
