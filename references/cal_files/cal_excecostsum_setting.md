# 期末余额汇总表参数设置-cal_excecostsum_setting

## 入库核算单据类型-多选基础资料表 t_cal_settinginbilltypes

- **表名称：** 入库核算单据类型-多选基础资料表
- **表名：** t_cal_settinginbilltypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_settinginbilltypes_pkey |  | fpkid |
| 2 | idx_cal_setinbt_id |  | fid |

---

## 采购入库类业务对象-多选基础资料表 t_calsetting_purbiztype

- **表名称：** 采购入库类业务对象-多选基础资料表
- **表名：** t_calsetting_purbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_calsetting_purbiztype_pkey |  | fpkid |
| 2 | idx_calsetting_purbt_fid |  | fid |

---

## 库存单据类型-多选基础资料表 t_cal_settingbilltype

- **表名称：** 库存单据类型-多选基础资料表
- **表名：** t_cal_settingbilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_settingbilltype |  | fpkid |
| 2 | idx_cal_settingbilltype_id |  | fid |

---

## 不更新核算余额的业务类型-多选基础资料表 t_calsetting_noupdbiztype

- **表名称：** 不更新核算余额的业务类型-多选基础资料表
- **表名：** t_calsetting_noupdbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_stnoupdbty |  | fpkid |

---

## 出库拆单类业务对象-多选基础资料表 t_calsettting_opbiztype

- **表名称：** 出库拆单类业务对象-多选基础资料表
- **表名：** t_calsettting_opbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_calsettting_opbiztype_pkey |  | fpkid |
| 2 | idx_calsetting_opbt_fid |  | fid |

---

## 出库核算单据类型-多选基础资料表 t_cal_settingoutbilltypes

- **表名称：** 出库核算单据类型-多选基础资料表
- **表名：** t_cal_settingoutbilltypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_settingoutbilltypes_pkey |  | fpkid |
| 2 | idx_cal_setoutbt_id |  | fid |

---

## 委外入库类业务对象-多选基础资料表 t_calsetting_ominbiztype

- **表名称：** 委外入库类业务对象-多选基础资料表
- **表名：** t_calsetting_ominbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_calsetting_ominbiztype |  | fpkid |
| 2 | pk_calsetting_ominbiztype_fid |  | fid |

---

## 出库类业务对象-多选基础资料表 t_calsettting_outbiztype

- **表名称：** 出库类业务对象-多选基础资料表
- **表名：** t_calsettting_outbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_calsetting_outbt_fid |  | fid |
| 2 | t_calsettting_outbiztype_pkey |  | fpkid |

---

## 允许零成本出入库的业务类型-多选基础资料表 t_calsetting_zerobiztype

- **表名称：** 允许零成本出入库的业务类型-多选基础资料表
- **表名：** t_calsetting_zerobiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_calsetting_zerobiztype_id |  | fid |
| 2 | pk_calsetting_zerobiztype |  | fpkid |

---

## 单据类型过滤条件匹配-多选基础资料表 t_calsetting_matbilltype

- **表名称：** 单据类型过滤条件匹配-多选基础资料表
- **表名：** t_calsetting_matbilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_calsetting_matbilltype_pkey |  | fpkid |
| 2 | idx_calsetting_matbt_fid |  | fid |

---

## 期末余额汇总表参数设置-主表 t_cal_setting

- **表名称：** 期末余额汇总表参数设置-主表
- **表名：** t_cal_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdividebasis | 划分依据 | varchar | 255 |  | √ | ' ' | 划分依据,枚举: |
| 3 | fentrynum | 出单分录数 | int8 | 64 |  | √ | 0 | 出单分录数 |
| 4 | fcostrecordextcols | 扩展字段 | varchar | 255 |  | √ | ' ' | 扩展字段,枚举: |
| 5 | fesstandards | 分摊标准 | varchar | 255 |  | √ | ' ' | 分摊标准,枚举: |
| 6 | fusenewplan | 启用新方案 | bpchar | 1 |  | √ | '0' | 启用新方案 |
| 7 | fesratetableid | fesratetableid | int8 | 64 |  | √ | 0 |  |
| 8 | faccountmethod | 存货记账方式 | bpchar | 1 |  | √ | '0' | 存货记账方式,枚举: 0 :库存单据 1 :核算成本记录 |
| 9 | fesconvertmode | fesconvertmode | bpchar | 1 |  | √ | '1' |  |
| 10 | fautoestimate | 自动暂估 | bpchar | 1 |  | √ | '0' | 自动暂估 |
| 11 | fbiztype | 核算单类型 | bpchar | 1 |  | √ | ' ' | 核算单类型,枚举: A :入库 B :出库 |
| 12 | fautoesstandard | 自动暂估分摊标准 | varchar | 255 |  | √ | ' ' | 自动暂估分摊标准,枚举: |
| 13 | fescurrencyid | fescurrencyid | int8 | 64 |  | √ | 0 |  |
| 14 | fcaldimension | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度,枚举: |
| 15 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_setting_cur |  | fescurrencyid |
| 2 | t_cal_setting_pkey |  | fid |

---

## 业务对象-多选基础资料表 t_calsetting_checkobject

- **表名称：** 业务对象-多选基础资料表
- **表名：** t_calsetting_checkobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_calsetting_checkobject_id |  | fid |
| 2 | pk_calsetting_checkobject |  | fpkid |

---

## 入库类业务对象-多选基础资料表 t_calsettting_inbiztype

- **表名称：** 入库类业务对象-多选基础资料表
- **表名：** t_calsettting_inbiztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_calsetting_inbt_fid |  | fid |
| 2 | t_calsettting_inbiztype_pkey |  | fpkid |
