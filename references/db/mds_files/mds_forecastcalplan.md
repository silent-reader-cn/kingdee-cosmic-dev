# 预测计划方案定义-mds_forecastcalplan

## 预测计划方案定义-主表 t_mds_forecastcalplan

- **表名称：** 预测计划方案定义-主表
- **表名：** t_mds_forecastcalplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foutlookperiod | 展望期（天） | int8 | 64 |  | √ | 0 | 展望期（天） |
| 3 | fcalstatus | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpredversion | 目标预测版本 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 8 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | frunninglog_tag | 运行日志_详情 | varchar | 2000 |  | √ | ' ' | 运行日志_详情 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmod | 计算百分比（%） | int8 | 64 |  | √ | 0 | 计算百分比（%） |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsourcetype | 预测来源类型 | varchar | 50 |  | √ | ' ' | 预测来源类型,枚举: mds_vrds :版本定义 mds_corl :预测关系记录 |
| 15 | fforecast | 预测 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 16 | fchangeway | 改写方式 | varchar | 50 |  | √ | ' ' | 改写方式,枚举: 0 :全部覆盖 1 :仅更新增加 |
| 17 | fbillno | 预测计划方案编码 | varchar | 80 |  | √ | ' ' | 预测计划方案编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fstype | 计算来源类型 | varchar | 5 |  | √ | ' ' | 计算来源类型,枚举: 0 :指定预测 1 :预测关系记录 |
| 20 | fdtype | 需求类型 | int8 | 64 |  | √ | 0 | 需求类型 mds_dmtp |
| 21 | fbillstatuscheckbox | 预测确认状态 | bpchar | 1 |  | √ | '0' | 预测确认状态 |
| 22 | frunninglog | 运行日志 | varchar | 255 |  | √ | ' ' | 运行日志 |

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

## 预测计划方案定义-多语言表 t_mds_forecastcalplan_l

- **表名称：** 预测计划方案定义-多语言表
- **表名：** t_mds_forecastcalplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 预测计划方案名称 | varchar | 100 |  | √ | ' ' | 预测计划方案名称 |
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
