# 全球财务雷达图方案规则-dfa_global_fin_radar_rule

## 全球财务雷达图方案规则-主表 t_dfa_global_finradarrule

- **表名称：** 全球财务雷达图方案规则-主表
- **表名：** t_dfa_global_finradarrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fupdate_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | frule_content | 规则内容 | varchar | 255 |  | √ | ' ' | 规则内容 |
| 4 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | frule_content_tag | 规则内容_详情 | text | 0 |  |  | null | 规则内容_详情 |
| 8 | fstock_type | 股票类型 | varchar | 50 |  | √ | ' ' | 股票类型,枚举: h-shares :港股 us-shares :美股 sgx-shares :新加坡股 a-shares :A股 three-shares :三板股 |
| 9 | flang | 语言环境 | varchar | 50 |  | √ | ' ' | 语言环境,枚举: zh-CN :中文简体 zh-TW :中文繁体 en-US :英文 ms-MY :马来语 vi-VN :越南语 th-TH :泰语 id-ID :印尼语 ar-001 :阿拉伯语 |
| 10 | fvalid | 是否生效 | bpchar | 1 |  | √ | '0' | 是否生效 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_global_finradarrule |  | fid |
