# 计划方案供需参数-pm_plansdparamdefault

## 计划方案供需参数-主表 t_pm_plansdparamdefault

- **表名称：** 计划方案供需参数-主表
- **表名：** t_pm_plansdparamdefault

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillformuladesc | 计算公式配置 | varchar | 512 |  | √ | ' ' | 计算公式配置 |
| 5 | fbillstatus | 生效状态 | varchar | 36 |  | √ | ' ' | 生效状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbillformula | 计算公式 | varchar | 512 |  | √ | ' ' | 计算公式 |
| 8 | fstockoutintype | 出入库类型 | varchar | 5 |  | √ | ' ' | 出入库类型,枚举: A :预计出+ B :预计出- C :预计入+ D :预计入- |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fentity | fentity | varchar | 36 |  | √ | ' ' |  |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_plansdparamdefault |  | fid |
| 2 | idx_pm_plansdparamdefault_fn |  | fnumber |

---

## 计划方案供需参数-多语言表 t_pm_plansdparamdefault_l

- **表名称：** 计划方案供需参数-多语言表
- **表名：** t_pm_plansdparamdefault_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_plansdparamdefault_l |  | fpkid |
| 2 | idx_pm_plansdparamdefault_l |  | fid |
