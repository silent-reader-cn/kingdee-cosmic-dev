# 引导语配置-mai_guideconfig

## 引导语配置-主表 t_mai_guideconfig

- **表名称：** 引导语配置-主表
- **表名：** t_mai_guideconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 引导语配置名称 | varchar | 30 |  | √ | ' ' | 引导语配置名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstatus | 可用状态 | bpchar | 1 |  | √ | '0' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置,枚举: 0 :否 1 :是 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 配置编号 | varchar | 30 |  | √ | ' ' | 配置编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_guideconfig |  | fid |
| 2 | idx_mai_guideconfig_fstatus |  | fstatus |

---

## 单据体-多语言表 t_mai_guideconfig_detail_l

- **表名称：** 单据体-多语言表
- **表名：** t_mai_guideconfig_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fguidewords | 引导语 | varchar | 200 |  | √ | ' ' | 引导语 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_guideconfig_detail_l |  | fpkid |
| 2 | idx_mai_guidecfg_dt_l_fentryid |  | fentryid |

---

## 引导语配置-多语言表 t_mai_guideconfig_l

- **表名称：** 引导语配置-多语言表
- **表名：** t_mai_guideconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 引导语配置名称 | varchar | 50 |  | √ | ' ' | 引导语配置名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_guideconfig_l_fid |  | fid |
| 2 | pk_t_mai_guideconfig_l |  | fpkid |

---

## 单据体-子表 t_mai_guideconfig_detail

- **表名称：** 单据体-子表
- **表名：** t_mai_guideconfig_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftype | 类型 | varchar | 10 |  | √ | ' ' | 类型,枚举: 查数值 :查数值 看趋势 :看趋势 做对比 :做对比 问排名 :问排名 |
| 4 | fguidewords | 引导语 | varchar | 200 |  | √ | ' ' | 引导语 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 6 | findicator | 指标 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_guidecfg_detail_fid |  | fid |
| 2 | pk_t_mai_guideconfig_detail |  | fentryid |
