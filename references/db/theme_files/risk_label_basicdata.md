# IPO风险标签下拉基础资料-risk_label_basicdata

## IPO风险标签下拉基础资料-主表 t_risk_label_basicdata

- **表名称：** IPO风险标签下拉基础资料-主表
- **表名：** t_risk_label_basicdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmulcombofield | 多选下拉列表 | varchar | 50 |  | √ | ' ' | 多选下拉列表,枚举: 1 :具体值 2 :阈值 3 :指标 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcombofield | 下拉列表 | varchar | 50 |  | √ | ' ' | 下拉列表,枚举: = :等于 != :不等于 in :在...中 not in :不在...中 > :大于 >= :大于等于 < :小于 <= :小于等于 1 :具体值 2 :阈值 3 :指标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_risk_label_basicdata_name |  | fname |
| 2 | pk_risk_label_basicdata |  | fid |

---

## IPO风险标签下拉基础资料-多语言表 t_risk_label_basicdata_l

- **表名称：** IPO风险标签下拉基础资料-多语言表
- **表名：** t_risk_label_basicdata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_risk_label_basicdata_l |  | fpkid |
| 2 | idx_label_basicdata_lname |  | flocaleid,fname |
