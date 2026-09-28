# 凭证参数设置-gl_voucherargs

## 凭证参数设置-主表 t_gl_voucherargs

- **表名称：** 凭证参数设置-主表
- **表名：** t_gl_voucherargs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisautomovedown | 审核后自动下移 | bpchar | 1 |  | √ | '0' | 审核后自动下移 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fqtypricerecalrule | 数量单价反算规则 | bpchar | 1 |  | √ | ' ' | 数量单价反算规则,枚举: 0 :不反算 1 :反算数量 2 :反算单价 |
| 5 | fupdaterate | 更新凭证汇率及本位币金额 | bpchar | 1 |  | √ | '0' | 更新凭证汇率及本位币金额 |
| 6 | fisusesystime | 新增凭证取系统日期 | bpchar | 1 |  | √ | '0' | 新增凭证取系统日期 |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ffocuskey | 光标默认位置 | varchar | 36 |  | √ | ' ' | 光标默认位置,枚举: book :账簿 attachment :附件 bizdate :业务日期 bookeddate :记账日期 edescription :摘要 account :科目 |
| 9 | fshowfullname | 显示科目全名 | bpchar | 1 |  | √ | '0' | 显示科目全名 |
| 10 | fisautobalance | 自动平衡 | bpchar | 1 |  | √ | '0' | 自动平衡 |
| 11 | foriraterecalrule | 原币汇率反算规则 | bpchar | 1 |  | √ | ' ' | 原币汇率反算规则,枚举: 0 :不反算 1 :反算原币 2 :反算汇率 |
| 12 | fratebybizdate | 按业务日期取汇率 | bpchar | 1 |  | √ | '0' | 按业务日期取汇率 |
| 13 | fexpiredate | 到期日 | bpchar | 1 |  | √ | '0' | 到期日,枚举: 0 :记账日期 1 :业务日期 2 :系统日期 |
| 14 | fisautosave | 自动保存 | bpchar | 1 |  | √ | '0' | 自动保存 |
| 15 | frightcontrolmodel | 侧边栏控制模式 | bpchar | 1 |  | √ | '0' | 侧边栏控制模式,枚举: 0 :自动 1 :折叠 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_voucherargs |  | forgid,fuserid |
| 2 | t_gl_voucherargs_pkey |  | fid |
