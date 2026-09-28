# 助手-gai_gpt_assistant_config

## 助手-主表 t_gai_assistant_config

- **表名称：** 助手-主表
- **表名：** t_gai_assistant_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpersona | 助手人设 | varchar | 50 |  |  | ' ' | 助手人设 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fintroduce | 自我介绍 | varchar | 255 |  | √ | ' ' | 自我介绍 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fchatsessiontag | 会话状态标签 | varchar | 255 |  | √ | ' ' | 会话状态标签 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fall_staff_assistant | 复选框-全员助手 | bpchar | 1 |  |  | '0' | 复选框-全员助手 |
| 11 | fswitchvoice | 复选框 | varchar | 1 |  |  | '0' | 复选框 |
| 12 | fisguest | 复选框-全员助手 | bpchar | 1 |  |  | '0' | 复选框-全员助手 |
| 13 | fopeningspeech | 简介 | varchar | 50 |  |  | ' ' | 简介 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fradiogroupfield | 单选按钮组 | varchar | 50 |  |  | ' ' | 单选按钮组,枚举: 0 :有创意的风格 1 :平衡的风格 2 :精准的风格 |
| 16 | fpicture | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 17 | ftype | 类型 | varchar | 50 |  |  | 'B' | 类型,枚举: A :侧边栏 B :自定义 C :H5 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fllm | 模型下拉列表 | varchar | 100 |  |  | ' ' | 模型下拉列表,枚举: |
| 20 | fenable | 启用 | varchar | 50 |  |  | '0' | 启用,枚举: 1 :可用 0 :已禁用 |
| 21 | fpicturefield | 官方自定义 | varchar | 255 |  | √ | ' ' | 官方自定义 |
| 22 | fnumber | 编码 | varchar | 30 |  |  | ' ' | 编码 |
| 23 | fprompt | 提示词 | int8 | 64 |  | √ | 0 | [提示词 gai_prompt](../gai_files/gai_prompt.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_assistant_config |  | fid |
| 2 | idx_gai_assistant_config |  | fname |

---

## 助手-多语言表 t_gai_assistant_config_l

- **表名称：** 助手-多语言表
- **表名：** t_gai_assistant_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fpersona | 助手人设 | varchar | 255 |  | √ | ' ' | 助手人设 |
| 4 | fintroduce | 自我介绍 | varchar | 255 |  | √ | ' ' | 自我介绍 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fopeningspeech | 简介 | varchar | 255 |  | √ | ' ' | 简介 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_assistant_config_l |  | fpkid |
| 2 | idx_gai_assistant_config_l_0 |  | fid,flocaleid |
