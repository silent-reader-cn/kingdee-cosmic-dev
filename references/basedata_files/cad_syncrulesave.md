# 同步制造规则归档-cad_syncrulesave

## 同步制造规则归档-主表 t_bd_syncrulesv

- **表名称：** 同步制造规则归档-主表
- **表名：** t_bd_syncrulesv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatfilter | 物料主数据信息 | varchar | 2000 |  | √ | ' ' | 物料主数据信息 |
| 3 | fmatfilter_tag | 物料主数据信息_详情 | text | 0 |  |  | null | 物料主数据信息_详情 |
| 4 | fbomtypeid | BOM类型 | int8 | 64 |  | √ | 0 | BOM类型 |
| 5 | fismainprocroute | 主工艺路线 | bpchar | 1 |  | √ | '1' | 主工艺路线 |
| 6 | fisincrementsync | 增量同步 | bpchar | 1 |  | √ | '0' | 增量同步 |
| 7 | fislatestaudittime | 最新审核日期 | bpchar | 1 |  | √ | '1' | 最新审核日期 |
| 8 | fsavetype | 保存类型 | varchar | 30 |  | √ | ' ' | 保存类型,枚举: A :同步成本BOM B :同步制造工艺路线 |
| 9 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fprocesstype | 工艺类型： | varchar | 30 |  | √ | ' ' | 工艺类型：,枚举: A :物料 B :物料组 C :通用 |
| 11 | fisreplace | 包含替代件 | bpchar | 1 |  | √ | '0' | 包含替代件 |
| 12 | fisjumplevel | 包含跳层 | bpchar | 1 |  | √ | '0' | 包含跳层 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_syncrulesv |  | fuserid |
| 2 | pk_t_bd_syncrulesv |  | fid |
