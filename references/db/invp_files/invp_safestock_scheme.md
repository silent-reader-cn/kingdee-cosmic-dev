# 安全库存统计方案-invp_safestock_scheme

## 安全库存统计方案-多语言表 t_invp_ssdayscheme_l

- **表名称：** 安全库存统计方案-多语言表
- **表名：** t_invp_ssdayscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_ssdayscheme_l |  | fpkid |
| 2 | idx_invp_ssdayscheme_l |  | fid,flocaleid |

---

## 安全库存统计方案-使用范围表 t_invp_ssdayscheme_u

- **表名称：** 安全库存统计方案-使用范围表
- **表名：** t_invp_ssdayscheme_u

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
| 1 | pk_t_invp_ssdayscheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_ssdayscheme_u_uo |  | fuseorgid |

---

## 业务组织-多选基础资料表 t_invp_safestockorg

- **表名称：** 业务组织-多选基础资料表
- **表名：** t_invp_safestockorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_safestock_org |  | fid |
| 2 | pk_t_invp_safestockorg |  | fpkid |

---

## 安全库存统计方案-主表 t_invp_ssdayscheme

- **表名称：** 安全库存统计方案-主表
- **表名：** t_invp_ssdayscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftracedays | 统计N天历史数据 | int8 | 64 |  | √ | 0 | 统计N天历史数据 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fconsumptionmodelid | 安全库存模型 | int8 | 64 |  | √ | 0 | 资源注册模型 invp_model_register |
| 6 | fservicelevel | 客户服务水平（%） | varchar | 30 |  | √ | ' ' | 客户服务水平（%） |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fplangroupid | 计划组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fcoefficient | 安全系数 | numeric | 23 | 10 | √ | 0 | 安全系数 |
| 15 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fdemmappingid | 匹配维度映射 | int8 | 64 |  | √ | 0 | 匹配映射配置 invp_matchmapping_config |
| 19 | fupdatetype | 安全库存记录更新方式 | varchar | 30 |  | √ | ' ' | 安全库存记录更新方式,枚举: A :追加 B :覆盖 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fplanorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | finvlevelcol | 安全库存天数字段 | varchar | 50 |  | √ | ' ' | 安全库存天数字段 |
| 23 | fplannerid | 计划员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 24 | fselectrulejson | 取数条件（json） | varchar | 512 |  | √ | ' ' | 取数条件（json） |
| 25 | finvlevelcolsign | 安全库存天数字段标识 | varchar | 50 |  | √ | ' ' | 安全库存天数字段标识 |
| 26 | finvlevelid | finvlevelid | int8 | 64 |  | √ | 0 |  |
| 27 | fcalplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 28 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | fmainplantype | 计划类型 | varchar | 10 |  | √ | ' ' | 计划类型,枚举: A :再订货点 B :最大最小 D :固定期间 |
| 30 | fselectrulejson_tag | 取数条件（json）_详情 | text | 0 |  |  | null | 取数条件（json）_详情 |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fselectruleformula_tag | 取数条件（表达式）_详情 | text | 0 |  |  | null | 取数条件（表达式）_详情 |
| 33 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 34 | fselectruleformula | 取数条件（表达式） | varchar | 512 |  | √ | ' ' | 取数条件（表达式） |
| 35 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 36 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | 库存水位维度 msplan_plan_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_invp_ssdayscheme_master |  | fmasterid |
| 2 | pk_t_invp_ssdayscheme |  | fid |
| 3 | idx_invp_ssdayscheme_orgnum |  | fplanorgid,fnumber |
| 4 | idx_t_invp_ssdayscheme_createorg |  | fcreateorgid |
