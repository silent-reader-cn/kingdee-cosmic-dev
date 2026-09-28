# 定时获取成本方案-ar_autogaincostscheme

## 定时获取成本方案-主表 t_ar_autogaincostschem

- **表名称：** 定时获取成本方案-主表
- **表名：** t_ar_autogaincostschem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffiltertext_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 6 | fsourcebill | 来源单据 | varchar | 50 |  | √ | ' ' | 来源单据,枚举: ar_revcfmbill :收入成本确认单 ar_verifyrecord :勾稽记录 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ffiltertext | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fsheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fexceplandesc | 执行计划 | varchar | 255 |  | √ | ' ' | 执行计划 |
| 15 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_autogaincostschem |  | fid |
| 2 | idx_ar_gaincostschem_num |  | fnumber |

---

## 定时获取成本方案-多语言表 t_ar_autogaincostschem_l

- **表名称：** 定时获取成本方案-多语言表
- **表名：** t_ar_autogaincostschem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_autogaincostschem_l |  | fpkid |
| 2 | idx_ar_gaincostscheml_fid |  | fid,flocaleid |
