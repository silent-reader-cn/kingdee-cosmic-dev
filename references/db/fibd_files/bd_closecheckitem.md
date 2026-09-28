# 结账检查项记录-bd_closecheckitem

## 单据体-子表 t_bd_closecheckitementry

- **表名称：** 单据体-子表
- **表名：** t_bd_closecheckitementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fformquery | 过滤条件 | varchar | 255 |  |  | ' ' | 过滤条件 |
| 3 | fmessage | 提示信息 | varchar | 100 |  |  | ' ' | 提示信息 |
| 4 | fformnumber | 表单标识 | varchar | 50 |  | √ | ' ' | 表单标识 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcheckitem | 检查项 | varchar | 50 |  | √ | ' ' | 检查项 |
| 7 | fcheckstate | 检查项状态 | int8 | 64 |  | √ | 0 | 检查项状态 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmenuid | 菜单ID | varchar | 80 |  | √ | ' ' | 菜单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_closecheckitementry |  | fid |
| 2 | t_bd_closecheckitementry_pkey |  | fentryid |

---

## 结账检查项记录-主表 t_bd_closecheckitem

- **表名称：** 结账检查项记录-主表
- **表名：** t_bd_closecheckitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompany | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | faccountbooks | 子系统账簿 | varchar | 50 |  | √ | ' ' | 子系统账簿 |
| 5 | fsubsysformnum | 子系统表单标识 | varchar | 50 |  | √ | ' ' | 子系统表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_closecheckitem |  | fcompany,faccountbooks,fperiod |
| 2 | pk_t_bd_closecheckitem |  | fid |
