# 预置术语包-cts_termword_preset

## 预置术语包-主表 t_cts_termword_preset

- **表名称：** 预置术语包-主表
- **表名：** t_cts_termword_preset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | flanid | 语言种类 | int8 | 64 |  | √ | 0 | 语言种类 inte_language |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fremarks | 补充说明 | varchar | 255 |  | √ | ' ' | 补充说明 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 32 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | ftermpackname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 12 | fnumber | 编码 | varchar | 32 |  | √ | ' ' | 编码 |
| 13 | findustry | 行业大类 | varchar | 64 |  | √ | ' ' | 行业大类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_termword_preset |  | fid |
| 2 | idx_t_cts_term_pre |  | fnumber |

---

## 预置术语包-多语言表 t_cts_termword_preset_l

- **表名称：** 预置术语包-多语言表
- **表名：** t_cts_termword_preset_l

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
| 1 | pk_t_cts_termword_preset_l |  | fpkid |
| 2 | idx_t_cts_term_pres_l |  | fid |

---

## 所属云-多选基础资料表 t_cts_term_presetcloud

- **表名称：** 所属云-多选基础资料表
- **表名：** t_cts_term_presetcloud

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_term_presetcloud |  | fpkid |
| 2 | idx_t_cts_term_prclu |  | fid |
