# 成本归集配置方案-cad_costconfigplan

## 单据体-子表 t_cad_configinfoentity

- **表名称：** 单据体-子表
- **表名：** t_cad_configinfoentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcebillid | 源单 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fusestatus | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcostconfigid | 配置单编号 | int8 | 64 |  | √ | 0 | 成本归集配置单 cad_costcollectconfig |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_configinfoentity |  | fid |
| 2 | pk_t_cad_configinfoentity |  | fentryid |

---

## 成本归集配置方案-主表 t_cad_costconfigplan

- **表名称：** 成本归集配置方案-主表
- **表名：** t_cad_costconfigplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcostcalcdimensionid | 成本核算维度 | int8 | 64 |  | √ | 0 | 成本核算维度 cad_costcalcdimension |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 10 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcostbillid | 成本单据 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 14 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 15 | fenable | 使用状态 | varchar | 10 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fcalmethod | 成本计算方法 | varchar | 10 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 PZ :品种法 CU :生产线成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costconfigplan |  | fid |
| 2 | idx_cad_costconfigplan_dim |  | fcostcalcdimensionid |
| 3 | idx_cad_costconfigplan |  | fappnum,fenable,fcalmethod |
| 4 | idx_cad_costconfigplan_org |  | forgid |

---

## 成本归集配置方案-多语言表 t_cad_costconfigplan_l

- **表名称：** 成本归集配置方案-多语言表
- **表名：** t_cad_costconfigplan_l

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
| 1 | pk_t_cad_costconfigplan_l |  | fpkid |
| 2 | idx_cad_cconfigplan_l |  | fid,flocaleid |
