# 轻脚本分级控制-kingscript_level_control

## 单据体-子表 t_ks_control_script

- **表名称：** 单据体-子表
- **表名：** t_ks_control_script

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fscript_basedata | 轻脚本(隐藏) | varchar | 50 |  |  | null | 插件脚本编辑 ide_pluginscript |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ks_control_script_fid |  | fid |
| 2 | pk_t_ks_control_script |  | fentryid |

---

## 轻脚本分级控制-主表 t_ks_control

- **表名称：** 轻脚本分级控制-主表
- **表名：** t_ks_control

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 10 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fcontrol_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fcontrol_level | 管控等级 | varchar | 50 |  |  | null | 管控等级,枚举: G :全局级别 T :租户级别 M :模块级别 S :脚本级别 |
| 8 | flimit_runtime | 执行时间限定 (秒) | numeric | 23 | 10 |  | null | 执行时间限定 (秒) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodule | 管控模块 | varchar | 255 |  |  | null | 管控模块 |
| 12 | fcontrol_type | 管控类型 | varchar | 50 |  |  | null | 管控类型,枚举: 0 :执行时间 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ks_control |  | fid |
| 2 | idx_ks_control_fbill |  | fbillno |
