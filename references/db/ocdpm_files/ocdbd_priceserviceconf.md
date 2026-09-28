# 取价服务配置-ocdbd_priceserviceconf

## 取价服务配置-主表 t_ocdbd_psconf

- **表名称：** 取价服务配置-主表
- **表名：** t_ocdbd_psconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 场景名称 | varchar | 100 |  | √ | ' ' | 场景名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fscenedesc | 场景说明 | varchar | 255 |  | √ | ' ' | 场景说明 |
| 10 | fnumber | 场景编码 | varchar | 80 |  | √ | ' ' | 场景编码 |
| 11 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_psconf |  | fid |
| 2 | idx_ocdbd_psconf_num |  | fnumber |

---

## 扩展字段配置表-子表 t_ocdbd_psconfentry

- **表名称：** 扩展字段配置表-子表
- **表名：** t_ocdbd_psconfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fppentrystr | 价格字段分录标识 | varchar | 50 |  | √ | ' ' | 价格字段分录标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fvposition | 源字段位置 | bpchar | 1 |  | √ | 'H' | 源字段位置,枚举: H :单头 E :分录 |
| 5 | fppfieldkey | 价格字段标识 | varchar | 50 |  | √ | ' ' | 价格字段标识 |
| 6 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 7 | fvfieldkey | 源字段标识 | varchar | 50 |  | √ | ' ' | 源字段标识 |
| 8 | fvdatatype | 源字段类型 | bpchar | 1 |  | √ | 'A' | 源字段类型,枚举: A :基础资料 |
| 9 | fventrystr | 源字段分录标识 | varchar | 50 |  | √ | ' ' | 源字段分录标识 |
| 10 | fppposition | 价格字段位置 | bpchar | 1 |  | √ | 'H' | 价格字段位置,枚举: H :单头 E :分录 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmatchlogic | 匹配逻辑 | bpchar | 1 |  | √ | 'E' | 匹配逻辑,枚举: E :等于 S :自定义 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_psconfentry |  | fentryid |
| 2 | idx_ocdbd_psconfen_id |  | fid |

---

## 取价服务配置-多语言表 t_ocdbd_psconf_l

- **表名称：** 取价服务配置-多语言表
- **表名：** t_ocdbd_psconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 场景名称 | varchar | 100 |  | √ | ' ' | 场景名称 |
| 3 | fscenedesc | 场景说明 | varchar | 255 |  | √ | ' ' | 场景说明 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_psconf_id |  | fid |
| 2 | pk_ocdbd_psconf_l |  | fpkid |
