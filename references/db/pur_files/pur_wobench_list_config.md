# 业务工作台配置-pur_wobench_list_config

## 界面按钮配置-子表 t_pur_wobench_opsubentry

- **表名称：** 界面按钮配置-子表
- **表名：** t_pur_wobench_opsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foptargetobjcol | 操作标识 | varchar | 80 |  | √ | ' ' | 操作标识 |
| 2 | foptargetobjcolno | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fopisshow | 是否可见 | bpchar | 1 |  | √ | '0' | 是否可见 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_wobench_opsubentry |  | fdetailid |
| 2 | idx_pur_wobench_opsubentry |  | fentryid,fseq |

---

## 界面字段配置-子表 t_pur_wobench_subentry

- **表名称：** 界面字段配置-子表
- **表名：** t_pur_wobench_subentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftargetobjcol | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | ftargetobjcolno | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fisshow | 是否可见 | bpchar | 1 |  | √ | '0' | 是否可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_wobench_subentry |  | fentryid,fseq |
| 2 | pk_pur_wobench_subentry |  | fdetailid |

---

## 业务工作台配置-多语言表 t_pur_wobench_config_l

- **表名称：** 业务工作台配置-多语言表
- **表名：** t_pur_wobench_config_l

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
| 1 | pk_pur_wobench_config_l |  | fpkid |
| 2 | idx_pur_wobench_config_l |  | fid,flocaleid |

---

## 业务工作台配置-主表 t_pur_wobench_config

- **表名称：** 业务工作台配置-主表
- **表名：** t_pur_wobench_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fwobenchbill | 工作台标识 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fisperset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_wobench_config |  | fid |
| 2 | idx_pur_wobench_config |  | fwobenchbill,fisenable |

---

## 工作台页签-子表 t_pur_wobench_entry

- **表名称：** 工作台页签-子表
- **表名：** t_pur_wobench_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillfilter | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 3 | ftargetbill | 目标单据 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbillfilterjson_tag | 过滤条件（json）_详情 | text | 0 |  |  | null | 过滤条件（json）_详情 |
| 6 | fbillfilterjson | 过滤条件（json） | varchar | 255 |  | √ | ' ' | 过滤条件（json） |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftabno | 页签名称 | varchar | 255 |  | √ | ' ' | 页签名称 |
| 9 | ftab | 页签标识 | varchar | 80 |  | √ | ' ' | 页签标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_wobench_entry_fidfseq |  | fid,fseq |
| 2 | pk_pur_wobench_entry |  | fentryid |
