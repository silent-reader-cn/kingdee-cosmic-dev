# 序列号维度-bd_sndimension

## 序列号维度-多语言表 t_bd_sndimension_l

- **表名称：** 序列号维度-多语言表
- **表名：** t_bd_sndimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 维度项 | varchar | 50 |  | √ | ' ' | 维度项 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_sndimension_l |  | fpkid |
| 2 | idx_bd_snd_id |  | fid,flocaleid |

---

## 序列号维度-主表 t_bd_sndimension

- **表名称：** 序列号维度-主表
- **表名：** t_bd_sndimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 6 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsncheckrange | 唯一性校验范围 | varchar | 50 |  | √ | ' ' | 唯一性校验范围,枚举: ,0, :全局唯一 ,1, :组织内唯一 ,2, :物料内唯一 ,1,2, :组织内物料唯一 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fsystempreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 14 | frelcolumn | 序列号关联字段 | varchar | 50 |  | √ | ' ' | 序列号关联字段 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_sndimension |  | fnumber |
| 2 | pk_t_bd_sndimension |  | fid |
