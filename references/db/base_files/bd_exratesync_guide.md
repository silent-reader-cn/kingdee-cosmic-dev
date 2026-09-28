# 外部汇率同步协议记录-bd_exratesync_guide

## 外部汇率同步协议记录-多语言表 t_bd_exratesync_guide_l

- **表名称：** 外部汇率同步协议记录-多语言表
- **表名：** t_bd_exratesync_guide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 64 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 64 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_exrsyn_gui_l |  | fid |
| 2 | pk_t_bd_exratesync_guide_l |  | fpkid |

---

## 外部汇率同步协议记录-主表 t_bd_exratesync_guide

- **表名称：** 外部汇率同步协议记录-主表
- **表名：** t_bd_exratesync_guide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 64 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fname | fname | varchar | 64 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 64 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_exrsyn_guide |  | fnumber |
| 2 | pk_t_bd_exratesync_guide |  | fid |
