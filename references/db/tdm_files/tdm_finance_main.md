# 财务报表-tdm_finance_main

## 财务报表-主表 t_tdm_cwbb

- **表名称：** 财务报表-主表
- **表名：** t_tdm_cwbb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fpeirod | 税期 | varchar | 100 |  | √ | ' ' | 税期 |
| 4 | ftemplateid | 报表模板ID | numeric | 19 |  | √ | 0 | 报表模板ID |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbzorg | 编制单位 | varchar | 100 |  | √ | ' ' | 编制单位 |
| 7 | fsourcesystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统,枚举: ierp :苍穹 eas :EAS |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | ftemplatetype | 报表类型 | varchar | 50 |  | √ | ' ' | 模板类型 tctb_template_type |
| 10 | fadjperi | 调整期间 | varchar | 50 |  | √ | ' ' | 调整期间 |
| 11 | ftypeid | 财务报表类型ID | varchar | 100 |  | √ | ' ' | 财务报表类型ID |
| 12 | faccountbookstype | 账簿类型 | varchar | 50 |  | √ | ' ' | 账簿类型 |
| 13 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 14 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: xttb :系统同步 mbyr :模板引入 sgxz :手工新增 |
| 15 | fisadjust | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 16 | ftemplate | 模板 | int8 | 64 |  | √ | 0 | 报表模板 tdm_finance_template |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_cwbb_pkey |  | fid |
| 2 | idx_t_tdm_cwbb |  | forgid |
