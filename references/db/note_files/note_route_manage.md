# 银行接口路由-note_route_manage

## 银行接口路由-多语言表 t_note_route_manage_l

- **表名称：** 银行接口路由-多语言表
- **表名：** t_note_route_manage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 路由名称 | varchar | 100 |  | √ | '' | 路由名称 |
| 3 | flocaleid | flocaleid | varchar | 100 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 100 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_route_manage_l_pkey |  | fpkid |

---

## 业务接口调用集合单据体-子表 t_note_routes

- **表名称：** 业务接口调用集合单据体-子表
- **表名：** t_note_routes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | finterface_name | 执行接口 | int8 | 64 |  |  | null | [银行接口配置管理 ebg_code_less](../note_files/ebg_code_less.md) |
| 3 | finterface_count | 当前接口最大数量 | int8 | 64 |  |  | null | 当前接口最大数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finterface_code | 接口码 | varchar | 100 |  | √ | ' ' | 接口码 |
| 6 | fjudging_condition_desc1 | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 8 | finterface_condition | 匹配规则 | int8 | 64 |  |  | null | [匹配规则 ebg_judging_condition](../note_files/ebg_judging_condition.md) |
| 9 | fcombofield | 执行策略 | varchar | 100 |  | √ | ' ' | 执行策略,枚举: all :总是执行 condition :匹配规则执行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_routes_pkey |  | fentryid |

---

## 同步接口调用集合单据体-子表 t_note_routes_query

- **表名称：** 同步接口调用集合单据体-子表
- **表名：** t_note_routes_query

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fjudging_condition_desc11 | 说明 | varchar | 255 |  | √ | null | 说明 |
| 3 | finterface_name1 | 执行接口 | int8 | 64 |  |  | null | [银行接口配置管理 ebg_code_less](../note_files/ebg_code_less.md) |
| 4 | finterface_condition1 | 匹配规则 | int8 | 64 |  |  | null | [匹配规则 ebg_judging_condition](../note_files/ebg_judging_condition.md) |
| 5 | finterface_count1 | 当前接口最大数量 | int8 | 64 |  |  | null | 当前接口最大数量 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finterface_code1 | 接口码 | varchar | 100 |  | √ | null | 接口码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 9 | fcombofield1 | 执行策略 | varchar | 100 |  | √ | null | 执行策略,枚举: all :总是执行 condition :匹配规则执行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_routes_query_pkey |  | fentryid |

---

## 银行接口路由-主表 t_note_route_manage

- **表名称：** 银行接口路由-主表
- **表名：** t_note_route_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 路由名称 | varchar | 100 |  |  | ' ' | 路由名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  |  | null | [银行应用列表 note_bank_app_list](../note_files/note_bank_app_list.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsub_biz_type | 子业务类型 | int8 | 64 |  |  | null | [路由类型 note_route_type](../note_files/note_route_type.md) |
| 7 | fbiz_type | 业务类型 | varchar | 100 |  |  | ' ' | 业务类型,枚举: CREDIT :信用证 NOTE :电票 BALANCE :余额 DETAIL :明细 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbiz_count | 批次最大数量 | int8 | 64 |  |  | null | 批次最大数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 100 |  |  | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_note_route_manage_pkey |  | fid |
