# 高新项目清单-rdem_fzz_gx_xm

## 高新项目清单-主表 t_rdem_fzz_gx_xm

- **表名称：** 高新项目清单-主表
- **表名：** t_rdem_fzz_gx_xm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxmle | 研发项目类型 | varchar | 50 |  | √ | ' ' | 研发项目类型,枚举: |
| 3 | fsfkjjkc | 是否可加计扣除 | varchar | 50 |  | √ | ' ' | 是否可加计扣除,枚举: |
| 4 | fsbxmxxname | 归属申报项目名称 | varchar | 200 |  | √ | ' ' | 归属申报项目名称 |
| 5 | fyfxmxx | 研发项目 | int8 | 64 |  | √ | 0 | [研发项目信息 rdem_yfxmxx](../rdem_files/rdem_yfxmxx.md) |
| 6 | fsbxmxxnumber | 归属申报项目编号 | varchar | 200 |  | √ | ' ' | 归属申报项目编号 |
| 7 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fstart | 项目起始日期 | timestamp | 0 |  |  | null | 项目起始日期 |
| 9 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: |
| 11 | fbaseprojectname | 研发项目名称 | varchar | 200 |  | √ | ' ' | 研发项目名称 |
| 12 | fbaseprojectnumber | 研发项目编号 | varchar | 30 |  | √ | ' ' | 研发项目编号 |
| 13 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 14 | fsbxm | 申报项目 | int8 | 64 |  | √ | 0 | [申报项目信息 rdem_sbxmxx](../rdem_files/rdem_sbxmxx.md) |
| 15 | fend | 项目结束日期 | timestamp | 0 |  |  | null | 项目结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_fzz_gx_xm |  | fid |
| 2 | idx_rdem_fzz_gx_xm_m0 |  | fsbxm |
