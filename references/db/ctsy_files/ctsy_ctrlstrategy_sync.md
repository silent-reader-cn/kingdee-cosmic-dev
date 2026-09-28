# 基础资料使用关系同步记录-ctsy_ctrlstrategy_sync

## 基础资料使用关系同步记录-主表 t_ctsy_ctrlstrategy_sync

- **表名称：** 基础资料使用关系同步记录-主表
- **表名：** t_ctsy_ctrlstrategy_sync

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftraceid | 链路ID | varchar | 255 |  | √ | ' ' | 链路ID |
| 4 | foporgid | 操作组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foptype | 操作类型 | bpchar | 1 |  | √ | '0' | 操作类型,枚举: 0 :分配 1 :个性化 2 :取消分配 |
| 7 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fmsgid | MQ消息ID | varchar | 50 |  | √ | ' ' | MQ消息ID |
| 10 | fuid | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |
| 11 | fentityid | 基础资料标识 | varchar | 50 |  | √ | ' ' | 基础资料标识 |
| 12 | ftartenantnumber | 目标租户编码 | varchar | 255 |  | √ | ' ' | 目标租户编码 |
| 13 | fsyncstatus | 同步状态 | bpchar | 1 |  | √ | '0' | 同步状态,枚举: 0 :同步中 1 :已同步 2 :失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctsy_ctrlstrategy_sync |  | fid |
| 2 | idx_t_ctsy_ctrlstrategy_sync |  | fuid |

---

## 数据分录-子表 t_ctsy_ctrl_sync_data

- **表名称：** 数据分录-子表
- **表名：** t_ctsy_ctrl_sync_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrormsg | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 3 | fdataid | 数据ID | int8 | 64 |  | √ | 0 | 数据ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnumber | 数据编码 | varchar | 255 |  | √ | ' ' | 数据编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctsy_ctrl_sync_data |  | fid,fdataid |
| 2 | pk_t_ctsy_ctrl_sync_data |  | fentryid |

---

## 组织分录-子表 t_ctsy_ctrl_sync_org

- **表名称：** 组织分录-子表
- **表名：** t_ctsy_ctrl_sync_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrormsg | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 3 | forgid | 组织ID | int8 | 64 |  | √ | 0 | 组织ID |
| 4 | forgnumber | 组织编码 | varchar | 255 |  | √ | ' ' | 组织编码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctsy_ctrl_sync_org |  | fid,forgid |
| 2 | pk_t_ctsy_ctrl_sync_org |  | fentryid |
