# 成组关系配置-cal_billgroupsetting

## 成组关系配置-主表 t_cal_billgroupsetting

- **表名称：** 成组关系配置-主表
- **表名：** t_cal_billgroupsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fbizpluginid | 处理插件 | int8 | 64 |  | √ | 0 | [核算预置插件 cal_plugin](../cal_files/cal_plugin.md) |
| 4 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 5 | ftarweightfield | 权重字段 | varchar | 80 |  | √ | ' ' | 权重字段,枚举: |
| 6 | fbillfilterstr_tag | 单据过滤条件_详情 | text | 0 |  |  | null | 单据过滤条件_详情 |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fisreturnbill | 退回不成组 | bpchar | 1 |  | √ | '0' | 退回不成组 |
| 10 | fstatus | 状态 | varchar | 5 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcostdealtype | 成本处理方式 | bpchar | 1 |  | √ | 'A' | 成本处理方式,枚举: A :成本 B :单位成本 |
| 14 | fbillplugin | 过滤插件 | int8 | 64 |  | √ | 0 | [核算预置插件 cal_plugin](../cal_files/cal_plugin.md) |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 16 | fcostfields | 成组子要素ID集合 | varchar | 2000 |  | √ | ' ' | 成组子要素ID集合 |
| 17 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 20 | frbillfilterstr | 关联单据过滤条件 | varchar | 255 |  |  | null | 关联单据过滤条件 |
| 21 | frbillfilterstr_tag | 关联单据过滤条件_详情 | text | 0 |  |  | null | 关联单据过滤条件_详情 |
| 22 | fcostcolumn | 成组成本字段 | varchar | 80 |  | √ | 'materialcost' | 成组成本字段,枚举: materialcost :材料成本 processcost :委外费用 fee :采购成本 manufacturecost :制造费用 resource :人工费用 |
| 23 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [成组关系配置 cal_billgroupsetting](../cal_files/cal_billgroupsetting.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 26 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fbill | 目标单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 28 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 29 | fenabledate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 30 | fistaildiff | 尾差 | bpchar | 1 |  | √ | '0' | 尾差 |
| 31 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 32 | frbillplugin | 过滤插件 | int8 | 64 |  | √ | 0 | [核算预置插件 cal_plugin](../cal_files/cal_plugin.md) |
| 33 | frelationbill | 来源单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 34 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 36 | fbillfilterstr | 单据过滤条件 | varchar | 255 |  |  | null | 单据过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_billgroupset_calorg |  | fcalorgid |
| 2 | t_cal_billgroupsetting_pkey |  | fid |

---

## 成组成本子要素-多选基础资料表 t_cal_gs_subelement

- **表名称：** 成组成本子要素-多选基础资料表
- **表名：** t_cal_gs_subelement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_gssubelement_fid |  | fid |
| 2 | t_cal_gs_subelement_pkey |  | fpkid |

---

## 成组关系配置-多语言表 t_cal_billgroupsetting_l

- **表名称：** 成组关系配置-多语言表
- **表名：** t_cal_billgroupsetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_billgroupsetting_l_pkey |  | fpkid |
| 2 | idx_cal_billgroupsetting_l |  | fid,flocaleid |

---

## 单据体-子表 t_cal_billgroupentry

- **表名称：** 单据体-子表
- **表名：** t_cal_billgroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frbillfieldname | 来源单据字段名称 | varchar | 80 |  | √ | ' ' | 来源单据字段名称 |
| 3 | fbillfield | 目标单据字段 | varchar | 80 |  | √ | ' ' | 目标单据字段 |
| 4 | fbillfieldname | 目标单据字段名称 | varchar | 80 |  | √ | ' ' | 目标单据字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | frbillfield | 来源单据字段 | varchar | 80 |  | √ | ' ' | 来源单据字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_billgroupentry_pkey |  | fentryid |
| 2 | idx_cal_billgroupentry |  | fid |
