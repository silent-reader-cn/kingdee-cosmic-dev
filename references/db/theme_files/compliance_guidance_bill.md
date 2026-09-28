# IPO合规指引管理单据-compliance_guidance_bill

## IPO合规指引管理单据-主表 t_compliance_guidance_nam

- **表名称：** IPO合规指引管理单据-主表
- **表名：** t_compliance_guidance_nam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftabcontent_tag | 页签内容_详情 | text | 0 |  |  | null | 页签内容_详情 |
| 3 | fgroupid | 树节点id | varchar | 50 |  | √ | ' ' | 树节点id |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fcompliancelabelguide | 合规标签指引 | int8 | 64 |  |  | null | 合规标签指引 |
| 8 | frelatedtopics | 关联主题 | varchar | 50 |  | √ | ' ' | 关联主题 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fipoorgld | IPO主体 | int8 | 64 |  |  | null | IPO编制组织 ipo_org |
| 11 | fdefault | 是否预置 | bpchar | 1 |  | √ | '1' | 是否预置 |
| 12 | ftabname | 页签名称 | varchar | 50 |  | √ | ' ' | 页签名称 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ftabcontent | 页签内容 | varchar | 255 |  | √ | ' ' | 页签内容 |
| 15 | ftabcode | 页签编码 | varchar | 50 |  | √ | ' ' | 页签编码 |
| 16 | fisshow | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_compliance_guidance_nam |  | fcompliancelabelguide |
| 2 | pk_compliance_guidance_nam |  | fid |
