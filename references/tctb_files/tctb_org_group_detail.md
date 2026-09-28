# 汇总方案子表-tctb_org_group_detail

## 汇总方案子表-主表 t_tctb_org_group_detail

- **表名称：** 汇总方案子表-主表
- **表名：** t_tctb_org_group_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主表id | int8 | 64 |  | √ | 0 | 主表id |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgcode | 组织编码 | varchar | 100 |  | √ | ' ' | 组织编码 |
| 5 | parententryid | parententryid | int8 | 64 |  | √ | 0 |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fkdqjyqylx | fkdqjyqylx | varchar | 50 |  | √ | ' ' |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fissuesbb | fissuesbb | bpchar | 1 |  | √ | ' ' |  |
| 10 | fdeclaration | 申报方式 | varchar | 30 |  | √ | ' ' | 申报方式,枚举: 1 :独立 2 :汇总 3 :被汇总 |
| 11 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 12 | fcollectorg | fcollectorg | varchar | 100 |  |  | ' ' |  |
| 13 | forgname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 14 | fshareid | fshareid | bpchar | 1 |  | √ | ' ' |  |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fentrychangetype | fentrychangetype | varchar | 50 |  | √ | ' ' |  |
| 17 | flevelname | flevelname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_org_group_detail_pkey |  | fentryid |
| 2 | idx_t_tctb_org_group_detail |  | fid |
