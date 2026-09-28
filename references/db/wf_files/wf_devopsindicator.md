# 运维指标-wf_devopsindicator

## 运维指标-多语言表 t_wf_devopsindicator_l

- **表名称：** 运维指标-多语言表
- **表名：** t_wf_devopsindicator_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimdisplayvalue | 类别名称 | varchar | 255 |  | √ | ' ' | 类别名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_devopsindicator_l |  | fid,flocaleid |
| 2 | pk_wf_devopsindicator_l |  | fpkid |

---

## 运维指标-主表 t_wf_devopsindicator

- **表名称：** 运维指标-主表
- **表名：** t_wf_devopsindicator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 参数 | varchar | 1000 |  | √ | ' ' | 参数 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fsendtimes | 发送次数 | int4 | 32 |  | √ | 0 | 发送次数 |
| 5 | fdimdisplayvalue | 类别名称 | varchar | 255 |  | √ | ' ' | 类别名称 |
| 6 | fnumber | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 7 | fdimvalue | 类别 | varchar | 50 |  | √ | ' ' | 类别 |
| 8 | fcount | 数量 | int4 | 32 |  | √ | 0 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_devopsindicator |  | fid |
| 2 | idx_wf_devopsindicator_date |  | fcreatedate |
