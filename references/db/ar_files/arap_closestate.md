# 期末结账-arap_closestate

## 期末结账-分表 t_gl_closestate_a

- **表名称：** 期末结账-分表
- **表名：** t_gl_closestate_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fcheckoutmsg | 处理结果 | varchar | 510 |  | √ | ' ' | 处理结果 |
| 8 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_closestate_a_p |  | fperiodtypeid |
| 2 | pk_t_gl_closestate_a |  | fid |

---

## 期末结账-主表 t_gl_closestate

- **表名称：** 期末结账-主表
- **表名：** t_gl_closestate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fthisclosetime | 本次结账耗时 | int8 | 64 |  | √ | 0 | 本次结账耗时 |
| 3 | fclosestate | 结账状态 | bpchar | 1 |  | √ | '0' | 结账状态,枚举: 0 :默认 1 :成功 2 :失败 |
| 4 | fcompany | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fclosedate | 结账日期 | timestamp | 0 |  |  | null | 结账日期 |
| 6 | faccountbooks | 子系统账簿 | varchar | 50 |  | √ | ' ' | 子系统账簿 |
| 7 | fcloseuserid | 结账用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fclosedetailsid | 结账详情 | int8 | 64 |  | √ | 0 | 结账详情 |
| 9 | fisautoclose | fisautoclose | bpchar | 1 |  | √ | '0' |  |
| 10 | foperatetype | foperatetype | bpchar | 1 |  | √ | '0' |  |
| 11 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 12 | flinestate | 排队状态 | bpchar | 1 |  | √ | '0' | 排队状态,枚举: 0 :默认 1 :结账中 2 :队列中 3 :重排队 |
| 13 | fsubsysformnum | 子系统表单标识 | varchar | 50 |  | √ | ' ' | 子系统表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_closestate_pkey |  | fid |
| 2 | idx_gl_closestate |  | fcompany,fperiod,fsubsysformnum |
