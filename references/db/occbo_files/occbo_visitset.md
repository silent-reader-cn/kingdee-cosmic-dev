# 外勤设置-occbo_visitset

## 外勤设置-主表 t_occbo_visitset

- **表名称：** 外勤设置-主表
- **表名：** t_occbo_visitset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famapkey | 高德地图Key | varchar | 150 |  | √ | ' ' | 高德地图Key |
| 3 | fsignrangecontrol | 签到电子围栏 | bpchar | 1 |  | √ | 'A' | 签到电子围栏,枚举: A :按围栏控制打卡 B :不控制 |
| 4 | fsecuritycode | 高德SecurityJsCode | varchar | 150 |  | √ | ' ' | 高德SecurityJsCode |
| 5 | fsigntype | 签到要求 | bpchar | 1 |  | √ | 'A' | 签到要求,枚举: A :必须签到打卡 B :不打卡 |
| 6 | fsignrange | 打卡电子围栏(米) | int4 | 32 |  | √ | 0 | 打卡电子围栏(米) |
| 7 | fkpiid | KPI设置 | int8 | 64 |  | √ | 0 | KPI occbo_kpi_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_visitset |  | fid |
| 2 | idx_occbo_visitset |  | fsigntype |

---

## 使用角色-多选基础资料表 t_occbo_visitset_role

- **表名称：** 使用角色-多选基础资料表
- **表名：** t_occbo_visitset_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 全渠道用户角色 ocdbd_role |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_visitset_role |  | fentryid,fbasedataid |
| 2 | pk_occbo_visitset_role |  | fpkid |

---

## 拜访事务设置-子表 t_occbo_visitset_entry

- **表名称：** 拜访事务设置-子表
- **表名：** t_occbo_visitset_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvisitthings | 拜访事务 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | frelationentity | 关联对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_visitset_entry |  | fentryid |
| 2 | idx_occbo_visitset_entry |  | fvisitthings |
