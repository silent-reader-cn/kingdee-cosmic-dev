# 预测计算方案定义F7-mds_forecastcalplanf7

## 预测计算方案定义F7-主表 t_mds_forecastcalplan

- **表名称：** 预测计算方案定义F7-主表
- **表名：** t_mds_forecastcalplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foutlookperiod | 展望期（天） | int8 | 64 |  | √ | 0 | 展望期（天） |
| 3 | fcalstatus | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 4 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fpredversion | 目标预测版本 | int8 | 64 |  | √ | 0 | [版本定义 mds_vrds](../mds_files/mds_vrds.md) |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | frunninglog_tag | frunninglog_tag | varchar | 2000 |  | √ | ' ' |  |
| 10 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 11 | fmod | fmod | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fsourcetype | fsourcetype | varchar | 50 |  | √ | ' ' |  |
| 15 | fforecast | fforecast | int8 | 64 |  | √ | 0 |  |
| 16 | fchangeway | 改写方式 | varchar | 50 |  | √ | ' ' | 改写方式,枚举: 0 :全覆盖 1 :仅更新 |
| 17 | fbillno | 预测计算方案编码 | varchar | 80 |  | √ | ' ' | 预测计算方案编码 |
| 18 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 19 | fstype | 计算来源类型 | varchar | 5 |  | √ | ' ' | 计算来源类型,枚举: 0 :指定预测 1 :预测关系记录 |
| 20 | fdtype | fdtype | int8 | 64 |  | √ | 0 |  |
| 21 | fbillstatuscheckbox | fbillstatuscheckbox | bpchar | 1 |  | √ | '0' |  |
| 22 | frunninglog | frunninglog | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_forecastcalplan |  | fbillno |
| 2 | pk_t_mds_forecastcalplan |  | fid |

---

## 预测计算方案定义F7-多语言表 t_mds_forecastcalplan_l

- **表名称：** 预测计算方案定义F7-多语言表
- **表名：** t_mds_forecastcalplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 预测计算方案名称 | varchar | 100 |  | √ | ' ' | 预测计算方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_forecastcalplan_l |  | fpkid |
| 2 | idx_mds_forecastcalplan_l |  | fid,flocaleid |
