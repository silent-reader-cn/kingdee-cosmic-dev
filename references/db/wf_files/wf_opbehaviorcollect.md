# 运维数据收集-wf_opbehaviorcollect

## 运维数据收集-主表 t_wf_behaviorcollect

- **表名称：** 运维数据收集-主表
- **表名：** t_wf_behaviorcollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcategory | 指标类型 | varchar | 200 |  | √ | ' ' | 指标类型 |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 6 | fappnumber | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 9 | ftypename | 类型名称 | varchar | 255 |  | √ | ' ' | 类型名称 |
| 10 | ftotal | 总数 | int8 | 64 |  | √ | 0 | 总数 |
| 11 | fdim | 维度 | varchar | 50 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_behaviorcollect |  | fid |
| 2 | idx_wf_behavicoll_numbertype |  | fnumber,ftype |

---

## 运维数据收集-多语言表 t_wf_behaviorcollect_l

- **表名称：** 运维数据收集-多语言表
- **表名：** t_wf_behaviorcollect_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | ftypename | 类型名称 | varchar | 255 |  | √ | ' ' | 类型名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_behaviorcollect_l |  | fid,flocaleid |
| 2 | pk_wf_behaviorcollect_l |  | fpkid |
