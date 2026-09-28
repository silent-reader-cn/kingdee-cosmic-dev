# 工作经验与年限映射-recru_expmatch

## 工作经验与年限映射-主表 t_recru_expmatch

- **表名称：** 工作经验与年限映射-主表
- **表名：** t_recru_expmatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpositionexpid | 职位工作经验AI标签 | int8 | 64 |  | √ | 0 | [ai职位知识库 recru_ai_position](../recru_files/recru_ai_position.md) |
| 6 | fstdrsmexpid | 标准简历工作经验AI标签 | int8 | 64 |  | √ | 0 | [ai标准简历知识库 recru_ai_stdrsm](../recru_files/recru_ai_stdrsm.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 3 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftype | 类型 | varchar | 3 |  | √ | ' ' | 类型,枚举: 1 :职位 2 :标准简历 |
| 12 | fyear | 年限 | numeric | 23 | 10 | √ | 0 | 年限 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_expmatch |  | fid |
| 2 | idx_recru_expmatch_std |  | fstdrsmexpid |
| 3 | idx_recru_expmatch_pos |  | fpositionexpid |

---

## 工作经验与年限映射-多语言表 t_recru_expmatch_l

- **表名称：** 工作经验与年限映射-多语言表
- **表名：** t_recru_expmatch_l

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
| 1 | pk_recru_expmatch_l |  | fpkid |
| 2 | idx_recru_expmatch_l_fid |  | fid,flocaleid |
