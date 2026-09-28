# 成本归集配置单-sco_costcollectconfig

## 单据体-子表 t_sco_costruleinfoentity

- **表名称：** 单据体-子表
- **表名：** t_sco_costruleinfoentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostobjname | 成本核算对象字段名称 | varchar | 255 |  | √ | ' ' | 成本核算对象字段名称 |
| 3 | fcostobjfield | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 4 | fsrcbillname | 源单字段名称 | varchar | 512 |  | √ | ' ' | 源单字段名称 |
| 5 | fparsefield | 核算维度解析字段 | bpchar | 1 |  | √ | '0' | 核算维度解析字段 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcbillfield | 字段标识 | varchar | 512 |  | √ | ' ' | 字段标识 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_ruleinfoentity |  | fid |
| 2 | pk_sco_costruleinfoentity |  | fentryid |

---

## 成本归集配置单-主表 t_sco_costcollectconfig

- **表名称：** 成本归集配置单-主表
- **表名：** t_sco_costcollectconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcfieldid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 3 | fcostcalcdimensionid | 成本核算维度 | int8 | 64 |  | √ | 0 | [成本核算维度 sco_costcalcdimension](../sco_files/sco_costcalcdimension.md) |
| 4 | fworkactivityid | 作业活动 | varchar | 68 |  | √ | ' ' | [作业活动 cad_new_workactivity](../aca_files/cad_new_workactivity.md) |
| 5 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fcostaccountid | 成本主体 | varchar | 80 |  | √ | ' ' | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | ffilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 14 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 15 | fcostdriverid | 成本动因 | varchar | 80 |  | √ | ' ' | [费用分配标准 cad_costdriver](../aca_files/cad_costdriver.md) |
| 16 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 21 | fautogenerateobj | 自动生成成本核算对象 | bpchar | 1 |  | √ | '0' | 自动生成成本核算对象 |
| 22 | fmaterialgroupstdid | 物料分类标准 | varchar | 80 |  | √ | ' ' | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 23 | fcostbillid | 成本单据 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fsourcebillid | 源单 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 25 | fismergesource | 按源单汇总 | varchar | 30 |  | √ | ' ' | 按源单汇总 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 28 | fcalmethod | 成本计算方法 | varchar | 10 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 SO :分批法 PZ :品种法 FL :分类法 SW :服务工单 SP :服务项目 RE :重复制造 CU :自定义 |
| 29 | fmatchcostobj | 按源单ID匹配成本核算对象 | bpchar | 1 |  | √ | '0' | 按源单ID匹配成本核算对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costcollectconfig |  | fid |
| 2 | idx_sco_costcollectconfig |  | fnumber |

---

## 单据体-子表 t_sco_fieldmapentity

- **表名称：** 单据体-子表
- **表名：** t_sco_fieldmapentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段标识 | varchar | 510 |  | √ | ' ' | 源单字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcostfield | 成本单据字段标识 | varchar | 255 |  | √ | ' ' | 成本单据字段标识 |
| 5 | fsourcefieldname | 源单字段名称 | varchar | 510 |  | √ | ' ' | 源单字段名称 |
| 6 | fformuladesc | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 7 | fselectvalue | 取值 | varchar | 30 |  | √ | ' ' | 取值,枚举: 0 :源单字段 1 :计算公式 2 :固定值 |
| 8 | fsourcetype | 来源类型 | varchar | 255 |  | √ | ' ' | 来源类型,枚举: er_expenseitemedit :费用项目 bos_costcenter :成本中心 |
| 9 | fsourcedataid | 固定值 | varchar | 255 |  | √ | ' ' | 费用项目 er_expenseitemedit |
| 10 | fformula | 计算公式值 | varchar | 2000 |  | √ | ' ' | 计算公式值 |
| 11 | fcostfieldname | 成本单据字段名称 | varchar | 255 |  | √ | ' ' | 成本单据字段名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdefval | 固定值 | varchar | 255 |  | √ | ' ' | 固定值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_fieldmapentity |  | fentryid |
| 2 | idx_sco_fieldmapentity |  | fid |

---

## 成本归集配置单-多语言表 t_sco_costcollectconfig_l

- **表名称：** 成本归集配置单-多语言表
- **表名：** t_sco_costcollectconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_collectconfig_l |  | fid,flocaleid |
| 2 | pk_sco_costcollectconfig_l |  | fpkid |
