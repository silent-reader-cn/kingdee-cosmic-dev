# 资金池使用核销方案-occba_verifyplan

## 资金池使用核销方案-主表 t_occba_verifyplan

- **表名称：** 资金池使用核销方案-主表
- **表名：** t_occba_verifyplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | finrecordfilter | 上账流水过滤条件 | text | 0 |  |  | null | 上账流水过滤条件 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frecordentity | 关联流水对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | faudittime | faudittime | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | finrecordfilter_tag | 上账流水过滤条件_详情 | text | 0 |  |  | null | 上账流水过滤条件_详情 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 17 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_verifyplan |  | fid |
| 2 | idx_occba_verifyplan_no |  | fnumber |

---

## 资金池账户类型-多选基础资料表 t_occba_vp_accounttype

- **表名称：** 资金池账户类型-多选基础资料表
- **表名：** t_occba_vp_accounttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_vp_accounttype |  | fpkid |
| 2 | idx_occba_vp_accounttype_fbid |  | fid,fbasedataid |

---

## 关联数据源实体-子表 t_occba_vp_entry

- **表名称：** 关联数据源实体-子表
- **表名：** t_occba_vp_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoindatafs_tag | 数据块过滤设置条件_详情 | text | 0 |  |  | null | 数据块过滤设置条件_详情 |
| 3 | fjoinfsset | 数据块过滤设置 | text | 0 |  |  | null | 数据块过滤设置 |
| 4 | fcolmap | fcolmap | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fjoinblockstatus | 数据块状态 | bpchar | 1 |  | √ | '1' | 数据块状态 |
| 7 | fjoindatafs | 数据块过滤设置条件 | text | 0 |  |  | null | 数据块过滤设置条件 |
| 8 | fsrcentity | 实体对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_vp_entry_fid |  | fid |
| 2 | pk_occba_vp_entry |  | fentryid |

---

## 资金池使用核销方案-多语言表 t_occba_verifyplan_l

- **表名称：** 资金池使用核销方案-多语言表
- **表名：** t_occba_verifyplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_verifyplan_l |  | fpkid |
| 2 | idx_occba_verifyplan_l_flid |  | fid,flocaleid |

---

## 适用组织-多选基础资料表 t_occba_vp_useorgs

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_occba_vp_useorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_vp_useorgs |  | fpkid |
| 2 | idx_occba_vp_useorgs_fbid |  | fid,fbasedataid |
