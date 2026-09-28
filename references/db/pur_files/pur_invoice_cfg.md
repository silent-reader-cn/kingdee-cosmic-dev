# 开票方案配置-pur_invoice_cfg

## 开票方案配置-主表 t_pur_invoice_cfg

- **表名称：** 开票方案配置-主表
- **表名：** t_pur_invoice_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fwobenchlistentrykey | 通用字段分录标识 | varchar | 50 |  | √ | ' ' | 通用字段分录标识,枚举: |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fwobenchlistbillid | 通用实体标识 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | ftargetbillid | 目标单据标识 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 9 | fisenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftype | 工作台类别 | varchar | 50 |  | √ | ' ' | 工作台类别,枚举: invoice :开票 check :对账 saloutstock :发货 pmapply :申请 |
| 12 | forderindex | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 13 | fisperset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoice_cfg_ftarbillid |  | ftargetbillid |
| 2 | idx_pur_invoice_cfg_fno |  | fnumber |
| 3 | pk_pur_invoice_cfg |  | fid |
| 4 | idx_pur_invoice_cfg_fenable |  | fisenable,ftype |

---

## 数据处理-子表 t_pur_invoice_cfgentry

- **表名称：** 数据处理-子表
- **表名：** t_pur_invoice_cfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbotpruleid | BOTP转换规则 | varchar | 80 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 3 | fsourcebillid | 来源单据标识 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fpluginname | 数据过滤插件 | varchar | 255 |  | √ | ' ' | 数据过滤插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_invoice_cfgentry_fidse |  | fid,fseq |
| 2 | pk_pur_invoice_cfgentry |  | fentryid |

---

## 字段映射-子表 t_pur_invoice_cfgsubentry

- **表名称：** 字段映射-子表
- **表名：** t_pur_invoice_cfgsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftargetobjcol | 通用字段标识 | varchar | 100 |  | √ | ' ' | 通用字段标识 |
| 2 | fformuladesc | 计算公式 | varchar | 500 |  | √ | ' ' | 计算公式 |
| 3 | fsourcebillcol | 来源字段标识 | varchar | 100 |  | √ | ' ' | 来源字段标识 |
| 4 | fselectvalue | 取值方式 | varchar | 1 |  | √ | ' ' | 取值方式,枚举: 0 :源单字段 1 :计算公式 |
| 5 | fformula | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsourcebillcolno | 来源字段名称 | varchar | 255 |  | √ | ' ' | 来源字段名称 |
| 8 | fformula_tag | 计算公式json_详情 | text | 0 |  |  | null | 计算公式json_详情 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | ftargetobjcolno | 通用字段名称 | varchar | 255 |  | √ | ' ' | 通用字段名称 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fisshow | 可见 | bpchar | 1 |  | √ | '1' | 可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_invoice_cfgsubentry |  | fdetailid |
| 2 | idx_pur_invoice_cfgsubentry |  | fentryid,fseq |

---

## 开票方案配置-多语言表 t_pur_invoice_cfg_l

- **表名称：** 开票方案配置-多语言表
- **表名：** t_pur_invoice_cfg_l

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
| 1 | idx_pur_invoice_cfg_l |  | fid,flocaleid |
| 2 | pk_pur_invoice_cfg_l |  | fpkid |
