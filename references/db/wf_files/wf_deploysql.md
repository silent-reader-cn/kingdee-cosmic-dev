# 部署脚本-wf_deploysql

## 部署脚本-主表 t_wf_deploysql

- **表名称：** 部署脚本-主表
- **表名：** t_wf_deploysql

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorinfo | 错误信息 | text | 0 |  |  | null | 错误信息 |
| 3 | fissuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: proctpl :流程模板 |
| 5 | ffilecontent | 脚本内容 | text | 0 |  |  | null | 脚本内容 |
| 6 | ffilename | 脚本名称 | varchar | 100 |  | √ | ' ' | 脚本名称 |
| 7 | fexecutiontime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_deploysql_filename |  | ffilename |
| 2 | pk_wf_deploysql |  | fid |

---

## 脚本内容分录-子表 t_wf_deploysqldetail

- **表名称：** 脚本内容分录-子表
- **表名：** t_wf_deploysqldetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fcontent | 内容 | varchar | 2000 |  | √ | ' ' | 内容 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_deploysqldetail |  | fid |
| 2 | pk_wf_deploysqldetail |  | fentryid |
