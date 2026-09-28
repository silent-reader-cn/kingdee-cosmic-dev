# 库存查询_筛选方案-barcm_imfilterplan

## 库存查询_筛选方案-主表 t_barcm_imfilterplan

- **表名称：** 库存查询_筛选方案-主表
- **表名：** t_barcm_imfilterplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flistshowvalue_tag | 表格显示字段_详情 | text | 0 |  |  | ' ' | 表格显示字段_详情 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 5 | ffiltervalue | 过滤数据 | varchar | 255 |  | √ | ' ' | 过滤数据 |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsavetype | 保存类型 | varchar | 50 |  | √ | ' ' | 保存类型,枚举: 0 :过滤数据 1 :汇总字段 2 :表格显示字段 3 :扫描设置 4 :用户参数设置 |
| 9 | fdefaultplanflag | 是否默认方案 | bpchar | 1 |  | √ | ' ' | 是否默认方案 |
| 10 | ffiltervalue_tag | 过滤数据_详情 | text | 0 |  |  | ' ' | 过滤数据_详情 |
| 11 | fsummaryvalue_tag | 汇总字段_详情 | text | 0 |  |  | ' ' | 汇总字段_详情 |
| 12 | fsummaryvalue | 汇总字段 | varchar | 255 |  | √ | ' ' | 汇总字段 |
| 13 | flistshowvalue | 表格显示字段 | varchar | 255 |  | √ | ' ' | 表格显示字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_imfilterplan |  | fid |
