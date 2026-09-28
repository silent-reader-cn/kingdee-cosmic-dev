# 绑定业务插件-bos_bizextpluginbind

## 插件清单-分表 t_meta_bizextplugin_s

- **表名称：** 插件清单-分表
- **表名：** t_meta_bizextplugin_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenable | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态,枚举: 0 :已禁用 1 :已启用 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_meta_bizextplugin_s |  | fentryid |
| 2 | idx_meta_bizextplugin_sid |  | fid |

---

## 插件清单-子表 t_meta_bizextplugin

- **表名称：** 插件清单-子表
- **表名：** t_meta_bizextplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 插件说明 | varchar | 500 |  | √ | ' ' | 插件说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fissysdisable | 系统禁用 | bpchar | 1 |  | √ | '0' | 系统禁用 |
| 5 | fpluginclass | 插件 | varchar | 200 |  | √ | ' ' | 插件 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fisv | 开发商 | varchar | 200 |  | √ | ' ' | 开发商 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftype | 插件类型 | bpchar | 1 |  | √ | '0' | 插件类型,枚举: 0 :Java插件 1 :Js脚本插件 2 :Ts脚本插件 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizextplugin_no |  | fpluginclass |
| 2 | pk_meta_bizextplugin |  | fentryid |
| 3 | idx_meta_bizextplugin_id |  | fid |

---

## 绑定业务插件-主表 t_meta_bizextcase

- **表名称：** 绑定业务插件-主表
- **表名：** t_meta_bizextcase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务场景名称 | varchar | 200 |  | √ | ' ' | 业务场景名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | finterfacetype | 扩展接口类型 | bpchar | 1 |  | √ | 'J' | 扩展接口类型,枚举: J :自定义Java接口 E :通用的扩展接口 S :自定义脚本接口 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsample_tag | 插件开发说明_详情 | text | 0 |  |  | null | 插件开发说明_详情 |
| 7 | fisv | 开发商 | varchar | 200 |  | √ | ' ' | 开发商 |
| 8 | finterface | 扩展接口 | varchar | 200 |  | √ | ' ' | 扩展接口 |
| 9 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsample | 插件开发说明 | varchar | 255 |  | √ | ' ' | 插件开发说明 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 业务场景编码 | varchar | 200 |  | √ | ' ' | 业务场景编码 |
| 17 | fobjecttype | 所属业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizextcase_num |  | fnumber |
| 2 | pk_meta_bizextcase |  | fid |

---

## 绑定业务插件-多语言表 t_meta_bizextcase_l

- **表名称：** 绑定业务插件-多语言表
- **表名：** t_meta_bizextcase_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务场景名称 | varchar | 275 |  | √ | ' ' | 业务场景名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizextcase_l_id |  | fid |
| 2 | pk_meta_bizextcase_l |  | fpkid |
