# 自定义核算单配置-pca_collconfig_cust

## 字段映射-子表 t_pca_collfieldmapentity

- **表名称：** 字段映射-子表
- **表名：** t_pca_collfieldmapentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 源单字段标识 | varchar | 255 |  | √ | ' ' | 源单字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcostfield | 成本单据字段标识 | varchar | 50 |  | √ | ' ' | 成本单据字段标识 |
| 5 | fsourcefieldname | 源单字段名称 | varchar | 50 |  | √ | ' ' | 源单字段名称 |
| 6 | fformuladesc | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 7 | fselectvalue | fselectvalue | varchar | 50 |  | √ | ' ' |  |
| 8 | fformula | 计算公式值 | varchar | 2000 |  | √ | ' ' | 计算公式值 |
| 9 | fselectvaluetype | 取值类型 | varchar | 50 |  | √ | ' ' | 取值类型,枚举: 0 :源单字段 1 :计算公式 2 :固定值 |
| 10 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 11 | fcostfieldname | 成本单据字段名称 | varchar | 50 |  | √ | ' ' | 成本单据字段名称 |
| 12 | fparamfieldkey | 参数字段key | varchar | 255 |  | √ | ' ' | 参数字段key |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_collfieldmapentity |  | fentryid |
| 2 | idx_pca_collfieldmapentity_fk |  | fid,fseq |

---

## 自定义核算单配置-多语言表 t_pca_costcollectconfig_l

- **表名称：** 自定义核算单配置-多语言表
- **表名：** t_pca_costcollectconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollectconfig_l |  | fpkid |

---

## 自定义核算单配置-主表 t_pca_costcollectconfig

- **表名称：** 自定义核算单配置-主表
- **表名：** t_pca_costcollectconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | ' ' | 过滤条件_详情 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | ffieldscope | 源单字段范围 | varchar | 255 |  | √ | ' ' | 源单字段范围 |
| 14 | fcostbillid | 成本单据 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 16 | fsourcebillid | 源单 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fbasedatatype | 数据基础资料类型 | varchar | 255 |  | √ | ' ' | 数据基础资料类型 |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | ffilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 20 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 21 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_balanceentry_billid |  | fcostbillid,fsourcebillid |
| 2 | pk_pca_costcollectconfig |  | fid |
| 3 | idx_pca_costcollectconfig_num |  | fnumber |
