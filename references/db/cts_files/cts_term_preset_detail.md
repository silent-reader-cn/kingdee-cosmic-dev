# 预置术语详情-cts_term_preset_detail

## 预置术语详情-多语言表 t_cts_term_predetail_l

- **表名称：** 预置术语详情-多语言表
- **表名：** t_cts_term_predetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cts_term_pre_l |  | fid |
| 2 | pk_t_cts_term_predetail_l |  | fpkid |

---

## 预置术语详情-主表 t_cts_term_predetail

- **表名称：** 预置术语详情-主表
- **表名：** t_cts_term_predetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 32 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftermpresetid | 预置术语包 | int8 | 64 |  | √ | 0 | 预置术语包 cts_termword_preset |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | foldname | 原名称 | varchar | 80 |  | √ | ' ' | 原名称 |
| 9 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnewname | 新名称 | varchar | 80 |  | √ | ' ' | 新名称 |
| 11 | fnumber | 编码 | varchar | 32 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cts_term_predet |  | ftermpresetid |
| 2 | pk_t_cts_term_predetail |  | fid |
