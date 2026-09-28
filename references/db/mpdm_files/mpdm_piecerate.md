# 计件工价-mpdm_piecerate

## 维度值子单据体-子表 t_mpdm_piecerate_subentry

- **表名称：** 维度值子单据体-子表
- **表名：** t_mpdm_piecerate_subentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimensionid | 工价维度 | int8 | 64 |  | √ | 0 | [工价维度_f7 mpdm_pdimension_f7](../mpdm_files/mpdm_pdimension_f7.md) |
| 2 | fdimensionvalue | 维度值 | varchar | 200 |  | √ | ' ' | 维度值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_piecerate_subentry |  | fdetailid |
| 2 | mpdm_pie_subentry_e_idx |  | fentryid |
| 3 | mpdm_pie_subentry_v_idx |  | fdimensionvalue |

---

## 工价明细存储分录-多语言表 t_mpdm_piecerateentry_l

- **表名称：** 工价明细存储分录-多语言表
- **表名：** t_mpdm_piecerateentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcomment | fcomment | varchar | 1000 |  | √ | ' ' |  |
| 2 | fdyncontent | 动态字段存储(隐藏) | varchar | 2000 |  | √ | ' ' | 动态字段存储(隐藏) |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_piecerateentry_lid |  | fentryid,flocaleid |
| 2 | pk_mpdm_piecerateentry_l |  | fpkid |

---

## 工价维度-多选基础资料表 t_mpdm_piecerate_mudyn

- **表名称：** 工价维度-多选基础资料表
- **表名：** t_mpdm_piecerate_mudyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工价维度_f7 mpdm_pdimension_f7](../mpdm_files/mpdm_pdimension_f7.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_piecerate_mudyn |  | fpkid |
| 2 | idx_mpdm_piecerate_mudynid |  | fid,fbasedataid |

---

## 计件工价-多语言表 t_mpdm_piecerate_l

- **表名称：** 计件工价-多语言表
- **表名：** t_mpdm_piecerate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工价名称 | varchar | 500 |  | √ | ' ' | 工价名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_piecerate_l |  | fpkid |
| 2 | idx_mpdm_piecerate_lid |  | fid,flocaleid |

---

## 计件工价-使用范围表 t_mpdm_piecerate_u

- **表名称：** 计件工价-使用范围表
- **表名：** t_mpdm_piecerate_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_piecerate_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_piecerate_u |  | fdataid,fuseorgid |

---

## 计件工价-主表 t_mpdm_piecerate

- **表名称：** 计件工价-主表
- **表名：** t_mpdm_piecerate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fprworklaodtype | 计件工作量类型 | bpchar | 1 |  | √ | ' ' | 计件工作量类型,枚举: A :产品数量 B :活动工时 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fname | 工价名称 | varchar | 500 |  | √ | ' ' | 工价名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 21 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 工价编码 | varchar | 80 |  | √ | ' ' | 工价编码 |
| 24 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_piecerate |  | fid |
| 2 | idx_t_mpdm_piecerate_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_piecerate_master |  | fmasterid |
| 4 | idx_mpdm_piecerate_number |  | fnumber |

---

## 工价明细存储分录-子表 t_mpdm_piecerateentry

- **表名称：** 工价明细存储分录-子表
- **表名：** t_mpdm_piecerateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fjobid | 工种 | int8 | 64 |  | √ | 0 | [工种 mpdm_jobtype](../mpdm_files/mpdm_jobtype.md) |
| 5 | fdyncontent | 动态字段存储(隐藏) | varchar | 2000 |  | √ | ' ' | 动态字段存储(隐藏) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fqualifiedprice | 合格单价 | numeric | 23 | 10 | √ | 0 | 合格单价 |
| 8 | fworktimeprice | 工时单价 | numeric | 23 | 10 | √ | 0 | 工时单价 |
| 9 | fmaterialcprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 10 | fenddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 11 | fstartdate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 12 | fjoblevelid | 工种等级 | int8 | 64 |  | √ | 0 | [工种等级 mpdm_joblevel](../mpdm_files/mpdm_joblevel.md) |
| 13 | fpriceunit | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fprocesscodeid | 标准工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fdeductionprice | 工废扣款单价 | numeric | 23 | 10 | √ | 0 | 工废扣款单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_piecerateentry |  | fentryid |
| 2 | idx_mpdm_piecerateentry_id |  | fid |
