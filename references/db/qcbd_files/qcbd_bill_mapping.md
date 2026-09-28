# 质量单据映射配置-qcbd_bill_mapping

## 单据映射清单分录-子表 t_qcbd_mapping_entry

- **表名称：** 单据映射清单分录-子表
- **表名：** t_qcbd_mapping_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrysyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 3 | ftargetfield | 目标字段 | varchar | 255 |  | √ | ' ' | 目标字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmapref | 映射关系 | varchar | 20 |  | √ | ' ' | 映射关系,枚举: ONE_TO_ONE :一对一 MANY_TO_ONE :多对一 |
| 6 | fsrcfield | 源单字段 | varchar | 255 |  | √ | ' ' | 源单字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mapping_entry |  | fentryid |

---

## 质量单据映射配置-多语言表 t_qcbd_bill_mapping_l

- **表名称：** 质量单据映射配置-多语言表
- **表名：** t_qcbd_bill_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bill_mapping_l |  | fpkid |

---

## 质量单据映射配置-主表 t_qcbd_bill_mapping

- **表名称：** 质量单据映射配置-主表
- **表名：** t_qcbd_bill_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsrcbill | 源单单据 | int8 | 64 |  | √ | 0 | [质量业务对象设置 qcbd_mapping_entityobject](../qcbd_files/qcbd_mapping_entityobject.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ftargetbill | 目标单据 | int8 | 64 |  | √ | 0 | [质量业务对象设置 qcbd_mapping_entityobject](../qcbd_files/qcbd_mapping_entityobject.md) |
| 11 | fsystempreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bill_mapping |  | fid |
| 2 | uidx_bill_mapping_src_target |  | fsrcbill,ftargetbill |
