# 专家奖励F7-src_expertawardf7

## 专家奖励F7-主表 t_src_expertaward

- **表名称：** 专家奖励F7-主表
- **表名：** t_src_expertaward

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpertid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fisselfhelp | fisselfhelp | bpchar | 1 |  | √ | '0' |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 10 | fbillno | 奖励编号 | varchar | 30 |  | √ | ' ' | 奖励编号 |
| 11 | fitemtypeid | 类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 12 | fbizorg | fbizorg | varchar | 255 |  | √ | ' ' |  |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 16 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 17 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 18 | fgradeid | fgradeid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 22 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 25 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 26 | fitemname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_expertaward_fbillno |  | fbillno |
| 2 | pk_src_expertaward |  | fid |
| 3 | idx_src_expertaward_fexpertid |  | fexpertid |
