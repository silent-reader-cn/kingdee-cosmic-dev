# 标准简历-recru_standardresume

## 标准简历-多语言表 t_recru_standardresume_l

- **表名称：** 标准简历-多语言表
- **表名：** t_recru_standardresume_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsirm_standardresume_l |  | fid,flocaleid |
| 2 | pk_recru_standardresume_l |  | fpkid |

---

## 标准简历-主表 t_recru_standardresume

- **表名称：** 标准简历-主表
- **表名：** t_recru_standardresume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsyncstruc | 同步结构化简历 | varchar | 2 |  | √ | ' ' | 同步结构化简历,枚举: 10 :是 20 :否 |
| 6 | fresumeid | 简历信息 | int8 | 64 |  | √ | 0 | [简历库 recru_resume](../recru_files/recru_resume.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstructresumeid | 结构化简历 | int8 | 64 |  | √ | 0 | [结构化简历 recru_structresume](../recru_files/recru_structresume.md) |
| 9 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcontactemail | 邮箱 | varchar | 255 |  | √ | ' ' | 邮箱 |
| 13 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fcellphone | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_standardresume |  | fid |
| 2 | idx_recru_standardresume_resum |  | fresumeid |

---

## 关联的简历-子表 t_recru_stmdresumerel

- **表名称：** 关联的简历-子表
- **表名：** t_recru_stmdresumerel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fresumeid | 关联简历 | int8 | 64 |  | √ | 0 | [简历库 recru_resume](../recru_files/recru_resume.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_stmdresumerel |  | fentryid |
| 2 | idx_recru_stmdresumerel_fid |  | fid |
