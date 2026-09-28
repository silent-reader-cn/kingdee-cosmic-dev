# 联动分录设置-xkcr_linkage_setting

## 联动分录设置-多语言表 t_xkcr_linkage_setting_l

- **表名称：** 联动分录设置-多语言表
- **表名：** t_xkcr_linkage_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_linkage_setting_l_fid |  | fid |
| 2 | pk_xkcr_linkage_setting_l |  | fpkid |

---

## 指定范围单据体-子表 t_xkcr_linkage_scopetype

- **表名称：** 指定范围单据体-子表
- **表名：** t_xkcr_linkage_scopetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedatafield | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_linkage_scopetype_fid |  | fid |
| 2 | pk_xkcr_linkage_scopetype |  | fentryid |

---

## 联动分录设置-主表 t_xkcr_linkage_setting

- **表名称：** 联动分录设置-主表
- **表名：** t_xkcr_linkage_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisscope | 指定范围 | bpchar | 1 |  | √ | ' ' | 指定范围 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 13 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 14 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_linkage_setting |  | fid |
| 2 | idx_linkage_setting_number |  | fnumber |

---

## 联动配置明细-子表 t_xkcr_linkage_entry

- **表名称：** 联动配置明细-子表
- **表名：** t_xkcr_linkage_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetrptitem | 目标报表项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdirection | 方向 | bpchar | 1 |  | √ | ' ' | 方向,枚举: 1 :正向 2 :反向 |
| 5 | ftargetitemdatatype | 目标项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsrcrptitem | 来源报表项目 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 8 | fsrcitemdatatype | 来源项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_linkage_entry_fid |  | fid |
| 2 | pk_xkcr_linkage_entry |  | fentryid |
