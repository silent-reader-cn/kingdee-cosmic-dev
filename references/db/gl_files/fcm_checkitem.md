# 结账检查项-fcm_checkitem

## 结账检查项-主表 t_fcm_checkitem

- **表名称：** 结账检查项-主表
- **表名：** t_fcm_checkitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubbizappid | 子应用 | varchar | 20 |  | √ | ' ' | 子应用,枚举: |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fcheckbillid | 结账检查对象 | int8 | 64 |  | √ | 0 | [结账检查对象 fcm_checkingbill](../gl_files/fcm_checkingbill.md) |
| 12 | fenablechange | 是否允许修改 | bpchar | 1 |  | √ | '1' | 是否允许修改 |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fpluginparamjson | 插件参数 | varchar | 512 |  | √ | ' ' | 插件参数 |
| 15 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fiseffective | 生效 | bpchar | 1 |  | √ | '1' | 生效 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcheckmethod | 配置方式 | bpchar | 1 |  | √ | ' ' | 配置方式,枚举: 1 :自定义条件 2 :插件 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 21 | fcheckconditionjson | 检查条件JSON | varchar | 255 |  | √ | ' ' | 检查条件JSON |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fcheckpluginid | 插件 | int8 | 64 |  | √ | 0 | [检查项插件 fcm_plugin](../gl_files/fcm_plugin.md) |
| 24 | fbillviewid | 联查页面 | bpchar | 1 |  | √ | '1' | 联查页面,枚举: 1 :表单 2 :列表 |
| 25 | fcheckconditionexpr | 检查条件json(废弃) | varchar | 2000 |  | √ | ' ' | 检查条件json(废弃) |
| 26 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '6' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fsuggesttype | 控制级别 | bpchar | 1 |  | √ | '1' | 控制级别,枚举: 1 :警告 2 :不通过 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fcheckconditionjson_tag | 检查条件JSON_详情 | text | 0 |  |  | ' ' | 检查条件JSON_详情 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcm_checkitem |  | fnumber |
| 2 | idx_t_fcm_checkitem_createorg |  | fcreateorgid |
| 3 | idx_t_fcm_checkitem_master |  | fmasterid |
| 4 | pk_t_fcm_checkitem |  | fid |

---

## 结账检查项-使用范围表 t_fcm_checkitem_u

- **表名称：** 结账检查项-使用范围表
- **表名：** t_fcm_checkitem_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcm_checkitem_u_uo |  | fuseorgid |
| 2 | pk_t_fcm_checkitem_u |  | fdataid,fuseorgid |

---

## 结账检查项-多语言表 t_fcm_checkitem_l

- **表名称：** 结账检查项-多语言表
- **表名：** t_fcm_checkitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcm_checkitem_l |  | fid,flocaleid |
| 2 | pk_t_fcm_checkitem_l |  | fpkid |

---

## 结账检查项-使用范围位图表 t_fcm_checkitem_m

- **表名称：** 结账检查项-使用范围位图表
- **表名：** t_fcm_checkitem_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcm_checkitem_m |  | forgid |
