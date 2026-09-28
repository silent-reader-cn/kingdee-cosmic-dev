# 成本归集配置单-cad_costcollectconfig

## 成本归集配置单-多语言表 t_cad_costcollectconfig_l

- **表名称：** 成本归集配置单-多语言表
- **表名：** t_cad_costcollectconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costcollectconfig_l |  | fpkid |
| 2 | idx_cad_collectconfig_l |  | fid,flocaleid |

---

## 单据体-子表 t_cad_fieldmapentity

- **表名称：** 单据体-子表
- **表名：** t_cad_fieldmapentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段标识 | varchar | 255 |  | √ | ' ' | 源单字段标识 |
| 3 | fsourcefieldname | 源单字段名称 | varchar | 255 |  | √ | ' ' | 源单字段名称 |
| 4 | fformuladesc | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 5 | fselectvalue | 取值 | varchar | 30 |  | √ | ' ' | 取值,枚举: 0 :源单字段 1 :计算公式 2 :固定值 |
| 6 | fsourcetype | 来源类型 | varchar | 200 |  | √ | ' ' | 来源类型,枚举: er_expenseitemedit :费用项目 |
| 7 | fsourcedataid | 固定值 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 8 | fformula | 计算公式值 | varchar | 2000 |  | √ | ' ' | 计算公式值 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fcostfieldname | 成本单据字段名称 | varchar | 60 |  | √ | ' ' | 成本单据字段名称 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcostfield | 成本单据字段标识 | varchar | 60 |  | √ | ' ' | 成本单据字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_fieldmapentity |  | fentryid |
| 2 | idx_cad_fieldmapentity |  | fid |

---

## 成本归集配置单-主表 t_cad_costcollectconfig

- **表名称：** 成本归集配置单-主表
- **表名：** t_cad_costcollectconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcfieldid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 3 | fcostcalcdimensionid | 成本核算维度 | int8 | 64 |  | √ | 0 | [成本核算维度 cad_costcalcdimension](../aca_files/cad_costcalcdimension.md) |
| 4 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fappnum | 所属应用 | varchar | 50 |  |  | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 10 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | ffilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 12 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 13 | fmustmatchcostobject | 强制匹配成本核算对象 | bpchar | 1 |  | √ | '0' | 强制匹配成本核算对象 |
| 14 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 15 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | ' ' | 过滤条件_详情 |
| 19 | fautogenerateobj | 自动生成成本核算对象 | bpchar | 1 |  | √ | '0' | 自动生成成本核算对象 |
| 20 | fcostbillid | 成本单据 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fsourcebillid | 源单 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 22 | fenable | 使用状态 | varchar | 10 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fcalmethod | 成本计算方法 | varchar | 10 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 SO :分批法 PZ :品种法 |
| 25 | fmatchcostobj | 按源单ID匹配成本核算对象 | bpchar | 1 |  | √ | '0' | 按源单ID匹配成本核算对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costcollectconfig |  | fid |
| 2 | idx_cad_collectconfig_org |  | forgid |
| 3 | idx_cad_collectconfig_dime |  | fcostcalcdimensionid |
| 4 | idx_cad_collectconfig |  | fenable,fpreset,fappnum |

---

## 单据体-子表 t_cad_costruleinfoentity

- **表名称：** 单据体-子表
- **表名：** t_cad_costruleinfoentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostobjname | 成本核算对象字段名称 | varchar | 60 |  | √ | ' ' | 成本核算对象字段名称 |
| 3 | fcostobjfield | 字段标识 | varchar | 60 |  | √ | ' ' | 字段标识 |
| 4 | fsrcbillname | 源单字段名称 | varchar | 60 |  | √ | ' ' | 源单字段名称 |
| 5 | fparsefield | 核算维度解析字段 | bpchar | 1 |  | √ | '0' | 核算维度解析字段 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsrcbillfield | 字段标识 | varchar | 60 |  | √ | ' ' | 字段标识 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_ruleinfoentity |  | fid |
| 2 | pk_t_cad_costruleinfoentity |  | fentryid |
