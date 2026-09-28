# 分配&#x2f;局部共享日志列表-bos_log_operation_assign

## 分配&#x2f;局部共享日志列表-主表 t_log_base_assign

- **表名称：** 分配&#x2f;局部共享日志列表-主表
- **表名：** t_log_base_assign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbizobjname | 操作对象名 | varchar | 255 |  | √ | ' ' | 操作对象名 |
| 3 | fmodifybillid | 数据更新源单内码 | varchar | 36 |  | √ | ' ' | 数据更新源单内码 |
| 4 | forgid | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fclienttype | 客户端类型 | varchar | 30 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 |
| 6 | fbizappname | 应用名 | varchar | 255 |  | √ | ' ' | 应用名 |
| 7 | fmodifyfields | 数据更新字段 | varchar | 1020 |  | √ | ' ' | 数据更新字段 |
| 8 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 9 | fexecutiontype | 执行方式 | varchar | 255 |  | √ | ' ' | 执行方式 |
| 10 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 11 | fusername | 操作用户名 | varchar | 255 |  | √ | ' ' | 操作用户名 |
| 12 | fclientnamee | 客户端名称名 | varchar | 255 |  | √ | ' ' | 客户端名称名 |
| 13 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 14 | fopdescriptione | 操作描述名 | varchar | 255 |  | √ | ' ' | 操作描述名 |
| 15 | fmodifycontent | 数据更新内容 | varchar | 510 |  |  | null | 数据更新内容 |
| 16 | flogdata | 分配详细日志 | text | 0 |  |  | null | 分配详细日志 |
| 17 | fbizobjid | 操作对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | fexecutiontime | 耗时 | varchar | 255 |  | √ | ' ' | 耗时 |
| 19 | fopnametype | 操作名称类型 | varchar | 255 |  | √ | ' ' | 操作名称类型 |
| 20 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fmodifybillno | 数据更新源单编码 | varchar | 255 |  | √ | ' ' | 数据更新源单编码 |
| 22 | fplanname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 23 | fmodifycontent_tag | 数据更新内容_详情 | text | 0 |  |  | null | 数据更新内容_详情 |
| 24 | fplannumber | 方案编码 | varchar | 255 |  | √ | ' ' | 方案编码 |
| 25 | fclientip | 客户端地址 | varchar | 128 |  | √ | ' ' | 客户端地址 |
| 26 | fopnamee | 操作名称名 | varchar | 255 |  | √ | ' ' | 操作名称名 |
| 27 | fopendtime | 操作结束时间 | timestamp | 0 |  |  | null | 操作结束时间 |
| 28 | fexecutiontatus | 执行状态 | varchar | 255 |  | √ | ' ' | 执行状态 |
| 29 | forgname | 操作组织名 | varchar | 255 |  | √ | ' ' | 操作组织名 |
| 30 | flogdatapath | 分配详细日志文件路径 | varchar | 255 |  | √ | ' ' | 分配详细日志文件路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_log_base_assign |  | fid |
| 2 | idx_t_log_base_assign_time |  | foptime,fbizappid,fuserid |

---

## 分配&#x2f;局部共享日志列表-多语言表 t_log_base_assign_l

- **表名称：** 分配&#x2f;局部共享日志列表-多语言表
- **表名：** t_log_base_assign_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fopname | 操作名称 | varchar | 255 |  |  | ' ' | 操作名称 |
| 3 | fopdescription | 操作描述 | varchar | 255 |  |  | ' ' | 操作描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fclientname | 客户端名称 | varchar | 255 |  |  | ' ' | 客户端名称 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_base_assign_l_opdesc |  | fopdescription |
| 2 | pk_t_log_base_assign_l |  | fpkid |
| 3 | idx_log_base_assign_l_opname |  | fopname |
| 4 | idx_log_base_assign_l_fid |  | fid,flocaleid |
