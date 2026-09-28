# 其他类型操作日志-bos_log_operation_other

## 其他类型操作日志-主表 t_log_app_other

- **表名称：** 其他类型操作日志-主表
- **表名：** t_log_app_other

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbizobjname | 操作对象名 | varchar | 255 |  | √ | ' ' | 操作对象名 |
| 3 | fmodifybillid | 数据更新源单内码 | varchar | 36 |  | √ | ' ' | 数据更新源单内码 |
| 4 | forgid | 操作组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fclienttype | 客户端类型 | varchar | 30 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 api :接口 |
| 6 | fbizappname | 应用名 | varchar | 255 |  | √ | ' ' | 应用名 |
| 7 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmodifybillno | 数据更新源单编码 | varchar | 255 |  | √ | ' ' | 数据更新源单编码 |
| 9 | fmodifycontent_tag | 数据更新内容_详情 | text | 0 |  |  | null | 数据更新内容_详情 |
| 10 | fmodifyfields | 数据更新字段 | varchar | 1020 |  | √ | ' ' | 数据更新字段 |
| 11 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 12 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 13 | fusername | 操作用户名 | varchar | 255 |  | √ | ' ' | 操作用户名 |
| 14 | fclientip | 客户端地址 | varchar | 128 |  | √ | ' ' | 客户端地址 |
| 15 | fclientnamee | 客户端名称名 | varchar | 255 |  | √ | ' ' | 客户端名称名 |
| 16 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 17 | fopdescriptione | 操作描述名 | varchar | 255 |  | √ | ' ' | 操作描述名 |
| 18 | fmodifycontent | 数据更新内容 | varchar | 510 |  |  | null | 数据更新内容 |
| 19 | fopnamee | 操作名称名 | varchar | 255 |  | √ | ' ' | 操作名称名 |
| 20 | fbizobjid | 操作对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 21 | forgname | 操作组织名 | varchar | 255 |  | √ | ' ' | 操作组织名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_log_app_other |  | fid |
| 2 | idx_logv2_other_modifybillid |  | fmodifybillid |
| 3 | idx_logv2_other_optimeuser |  | foptime,fbizappid,fuserid |

---

## 其他类型操作日志-多语言表 t_log_app_other_l

- **表名称：** 其他类型操作日志-多语言表
- **表名：** t_log_app_other_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
