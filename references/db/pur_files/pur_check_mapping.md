# 对账映射配置-pur_check_mapping

## 对账映射配置-多语言表 t_pur_check_mapping_l

- **表名称：** 对账映射配置-多语言表
- **表名：** t_pur_check_mapping_l

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
| 1 | pk_pur_check_mapping_l |  | fpkid |
| 2 | idx_pur_check_mapping_l |  | fid,flocaleid |

---

## 字段映射-子表 t_pur_check_mfixedentry

- **表名称：** 字段映射-子表
- **表名：** t_pur_check_mfixedentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetobjcol | 对账中心字段标识 | varchar | 100 |  | √ | ' ' | 对账中心字段标识 |
| 3 | fformuladesc | 计算公式 | varchar | 500 |  | √ | ' ' | 计算公式 |
| 4 | fsourcebillcol | 来源字段标识 | varchar | 100 |  | √ | ' ' | 来源字段标识 |
| 5 | fselectvalue | 取值 | bpchar | 1 |  | √ | '0' | 取值,枚举: 0 :源单字段 1 :计算公式 |
| 6 | fformula | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsourcebillcolno | 来源字段名称 | varchar | 100 |  | √ | ' ' | 来源字段名称 |
| 9 | fformula_tag | 计算公式json_详情 | text | 0 |  |  | ' ' | 计算公式json_详情 |
| 10 | fispresit | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 11 | ftargetobjcolno | 对账中心字段名称 | varchar | 100 |  | √ | ' ' | 对账中心字段名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_check_mfixedentry |  | fentryid |
| 2 | idx_pur_check_mfixedentry |  | fid,fseq |

---

## 对账映射配置-主表 t_pur_check_mapping

- **表名称：** 对账映射配置-主表
- **表名：** t_pur_check_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsourcebill | 来源单据 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsourceentrykey | 来源分录标识 | varchar | 80 |  | √ | ' ' | 来源分录标识,枚举: |
| 8 | fchecktype | 对账类型 | bpchar | 1 |  | √ | '1' | 对账类型,枚举: 1 :按源单对账 2 :抵扣分摊 3 :费用分摊 |
| 9 | fisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用,枚举: 0 :禁用 1 :可用 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fisperset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fpluginname | 插件名称 | varchar | 255 |  | √ | ' ' | 插件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_check_mapping |  | fid |
| 2 | idx__pur_check_mapping |  | fsourcebill,fisenable |
